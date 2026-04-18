from typing import Sequence

import dlt

from google_sheets import google_spreadsheet


def load_pipeline_with_ranges(
    spreadsheet_url_or_id: str, range_names: Sequence[str]
) -> None:
    """
    Loads explicitly passed ranges
    """
    pipeline = dlt.pipeline(
        pipeline_name="google_sheets_pipeline",
        destination='motherduck',
        #dev_mode=True,
        dataset_name="sheets_vomit_inputs",
    )
    data = google_spreadsheet(
        spreadsheet_url_or_id=spreadsheet_url_or_id,
        range_names=range_names,
        get_sheets=False,
        get_named_ranges=False,
    )
    info = pipeline.run(data, table_name="sheets_mei_vomit_inputs")
    print(info)

if __name__ == "__main__":
    url_or_id = "1sx01sSnfVqaSRSZBpeudEif5tpztxGjkJta3GzLGza4"
    range_names = ["main"]

    load_pipeline_with_ranges(url_or_id, range_names)
