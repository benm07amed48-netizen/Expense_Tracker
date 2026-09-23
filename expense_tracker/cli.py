"""CLI entrypoint for the Expense Tracker app."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="expense-tracker")
    parser.description = "Expense Tracker CLI"
    return parser


def main() -> int:
    build_parser().parse_args()
    return 0
