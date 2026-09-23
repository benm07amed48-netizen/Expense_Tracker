"""Allow running the app with `python -m expense_tracker`."""

from expense_tracker.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
