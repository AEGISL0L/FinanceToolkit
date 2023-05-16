"""Efficiency Ratios Tests""" ""
import pandas as pd

from financialtoolkit.ratios import efficiency

# pylint: disable=missing-function-docstring


def test_get_asset_turnover_ratio(recorder):
    recorder.capture(
        efficiency.get_asset_turnover_ratio(
            sales=pd.Series([100, 110, 120, 130, 80]),
            total_assets=pd.Series([500, 400, 300, 200, 100]),
        )
    )


def test_get_inventory_turnover_ratio(recorder):
    recorder.capture(
        efficiency.get_inventory_turnover_ratio(
            cost_of_goods_sold=pd.Series([130, 120, 110, 150, 100]),
            average_inventory=pd.Series([150, 140, 120, 189, 100]),
        )
    )


def test_get_days_of_inventory_outstanding(recorder):
    recorder.capture(
        efficiency.get_days_of_inventory_outstanding(
            average_inventory=pd.Series([130, 120, 110, 150, 100]),
            cost_of_goods_sold=pd.Series([150, 140, 120, 189, 100]),
        )
    )

    recorder.capture(
        efficiency.get_days_of_inventory_outstanding(
            average_inventory=pd.Series([130, 120, 110, 150, 100]),
            cost_of_goods_sold=pd.Series([150, 140, 120, 189, 100]),
            days=30,
        )
    )


def test_get_days_of_sales_outstanding(recorder):
    recorder.capture(
        efficiency.get_days_of_sales_outstanding(
            accounts_receivable=pd.Series([130, 120, 110, 150, 100]),
            revenue=pd.Series([150, 140, 120, 189, 100]),
        )
    )

    recorder.capture(
        efficiency.get_days_of_sales_outstanding(
            accounts_receivable=pd.Series([130, 120, 110, 150, 100]),
            revenue=pd.Series([150, 140, 120, 189, 100]),
            days=30,
        )
    )


def test_get_operating_cycle(recorder):
    recorder.capture(
        efficiency.get_operating_cycle(
            days_of_inventory=pd.Series([20, 10, 20, 10, 30]),
            days_of_sales_outstanding=pd.Series([10, 19, 17, 18, 20.5]),
        )
    )


def test_get_accounts_payables_turnover_ratio(recorder):
    recorder.capture(
        efficiency.get_accounts_payables_turnover_ratio(
            cost_of_goods_sold=pd.Series([150, 140, 120, 189, 100]),
            average_accounts_payable=pd.Series([130, 120, 110, 150, 100]),
        )
    )


def test_get_days_of_accounts_payable_outstanding(recorder):
    recorder.capture(
        efficiency.get_days_of_accounts_payable_outstanding(
            cost_of_goods_sold=pd.Series([130, 120, 110, 150, 100]),
            average_accounts_payable=pd.Series([150, 140, 120, 189, 100]),
        )
    )

    recorder.capture(
        efficiency.get_days_of_accounts_payable_outstanding(
            cost_of_goods_sold=pd.Series([130, 120, 110, 150, 100]),
            average_accounts_payable=pd.Series([150, 140, 120, 189, 100]),
            days=30,
        )
    )


def test_get_cash_conversion_cycle(recorder):
    recorder.capture(
        efficiency.get_cash_conversion_cycle(
            days_inventory=pd.Series([20, 10, 20, 10, 30]),
            days_sales_outstanding=pd.Series([10, 19, 17, 18, 20.5]),
            days_payables_outstanding=pd.Series([8, 17, 10, 10, 20.1]),
        )
    )


def test_get_receivables_turnover(recorder):
    recorder.capture(
        efficiency.get_receivables_turnover(
            accounts_receivable=pd.Series([130, 120, 110, 150, 100]),
            revenue=pd.Series([150, 140, 120, 189, 100]),
        )
    )


def test_get_sga_to_revenue_ratio(recorder):
    recorder.capture(
        efficiency.get_sga_to_revenue_ratio(
            sga_expenses=pd.Series([130, 120, 110, 150, 100]),
            revenue=pd.Series([150, 140, 120, 189, 100]),
        )
    )


def test_get_fixed_asset_turnover(recorder):
    recorder.capture(
        efficiency.get_fixed_asset_turnover(
            revenue=pd.Series([150, 140, 120, 189, 100]),
            net_fixed_assets=pd.Series([1000, 1500, 1500, 1300, 800]),
        )
    )
