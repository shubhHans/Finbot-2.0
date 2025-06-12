import os
import pandas as pd

class DataProcessor:
    def __init__(self, df_alloc, df_financial) -> None:
        self.df_alloc = df_alloc
        self.df_financial = df_financial
        self.save_path = "processed/"
        self.alloc_filename = "allocations.csv"
        self.financial_filename = "financial.csv"

    def _handle_missing_values_alloc(self) -> None:
        # drop rows with missing client or allocation
        self.df_alloc = self.df_alloc[~self.df_alloc['Client'].isna()]
        self.df_alloc = self.df_alloc[~self.df_alloc['Target Allocation (%)'].isna()]
        # fill missing portfolio and asset class with 'Unknown'
        self.df_alloc[['Target Portfolio', 'Asset Class']] = self.df_alloc[
            ['Target Portfolio', 'Asset Class']
        ].fillna('Unknown')

    def _handle_missing_values_financial(self) -> None:
        # drop rows with missing client
        self.df_financial = self.df_financial[~self.df_financial['Client'].isna()]
        # fill non-critical fields with 'Unknown'
        self.df_financial[
            ['Symbol', 'Name', 'Sector', 'Purchase Date', 'Analyst Rating', 'Risk Level']
        ] = self.df_financial[
            ['Symbol', 'Name', 'Sector', 'Purchase Date', 'Analyst Rating', 'Risk Level']
        ].fillna('Unknown')
        # only drop rows missing essential numeric fields
        self.df_financial.dropna(subset=['Quantity', 'Buy Price', 'Current Price', 'Market Value'], inplace=True)

    def _handle_client_column_financial(self) -> None:
        # keep only clients that exist in allocations data
        self.df_financial = self.df_financial[
            self.df_financial['Client'].isin(self.df_alloc['Client'].unique())
        ]

    def _get_client_id(self) -> None:
        self._handle_client_column_financial()

        # if client names have underscore, simplify to id; otherwise keep as is
        self.df_alloc['Client'] = self.df_alloc['Client'].apply(
            lambda x: x.split('_')[1] if '_' in x else x
        )
        self.df_financial['Client'] = self.df_financial['Client'].apply(
            lambda x: x.split('_')[1] if '_' in x else x
        )

    def save_processed_data(self) -> None:
        # Create directory if it doesn't exist
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Apply preprocessing steps
        self._handle_missing_values_alloc()
        self._handle_missing_values_financial()
        self._get_client_id()

        # Save cleaned data
        self.df_alloc.to_csv(self.save_path + self.alloc_filename, index=False)
        self.df_financial.to_csv(self.save_path + self.financial_filename, index=False)
