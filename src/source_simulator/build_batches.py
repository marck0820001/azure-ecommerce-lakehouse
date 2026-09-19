from pathlib import Path
import shutil

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw_original"
SIMULATOR_DIR = PROJECT_ROOT / "data" / "source_simulator"

INITIAL_DIR = SIMULATOR_DIR / "initial"
INCREMENTAL_DIR = SIMULATOR_DIR / "incremental"

DIMENSION_FILES = [
    "olist_customers_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]


def create_directories() -> None:
    INITIAL_DIR.mkdir(parents=True, exist_ok=True)
    INCREMENTAL_DIR.mkdir(parents=True, exist_ok=True)


def copy_initial_dimensions() -> None:
    print("Creating initial dimension load...")

    for filename in DIMENSION_FILES:
        source = RAW_DIR / filename
        destination = INITIAL_DIR / filename

        if not source.exists():
            raise FileNotFoundError(source)

        shutil.copy2(source, destination)

        print(f"Copied: {filename}")


def create_incremental_batches() -> None:
    print("\nLoading transactional datasets...")

    orders = pd.read_csv(
        RAW_DIR / "olist_orders_dataset.csv",
        parse_dates=["order_purchase_timestamp"],
    )

    items = pd.read_csv(RAW_DIR / "olist_order_items_dataset.csv")

    payments = pd.read_csv(RAW_DIR / "olist_order_payments_dataset.csv")

    orders["batch_month"] = (
        orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
    )

    months = sorted(orders["batch_month"].dropna().unique())

    print(f"Number of batches: {len(months)}")

    for month in months:
        print(f"\nCreating batch: {month}")

        batch_dir = INCREMENTAL_DIR / f"batch_month={month}"

        batch_dir.mkdir(parents=True, exist_ok=True)

        orders_batch = orders[orders["batch_month"] == month].copy()

        order_ids = set(orders_batch["order_id"])

        items_batch = items[items["order_id"].isin(order_ids)].copy()

        payments_batch = payments[payments["order_id"].isin(order_ids)].copy()

        orders_batch.drop(columns=["batch_month"], inplace=True)

        orders_batch.to_csv(batch_dir / "orders.csv", index=False)

        items_batch.to_csv(batch_dir / "order_items.csv", index=False)

        payments_batch.to_csv(batch_dir / "order_payments.csv", index=False)

        print(
            f"orders={len(orders_batch):,} | "
            f"items={len(items_batch):,} | "
            f"payments={len(payments_batch):,}"
        )


def main() -> None:
    create_directories()
    copy_initial_dimensions()
    create_incremental_batches()

    print("\nSource simulation completed.")


if __name__ == "__main__":
    main()
