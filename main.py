import gee_lib.gee_lib as gee


my_df = gee.GoogleEarthEngine()
my_df.set_collection_date_range(date_range=['2020-01-01T00:00:00', '2020-12-31T00:00:00'])
my_df.set_collection_geometry_from_gee_country_str('Greece')
my_df.set_collection(dataset_id=gee.GSV_DS_LANDSAT_7_RAW_T1_KEY)
gee.prt_dict_full_dataset(dataset_id=gee.GSV_DS_LANDSAT_7_RAW_T1_KEY)
