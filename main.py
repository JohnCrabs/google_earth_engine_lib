import gee_lib.gee_lib as gee


my_df = gee.GoogleEarthEngine()
my_df.set_collection_date_range(date_range=['2020-06-01T00:00:00', '2020-06-14T00:00:00'])
my_df.set_collection_geometry_from_gee_country_str('Greece')
my_df.set_collection(dataset_id=gee.GSV_DS_LANDSAT_8_RAW_T1_KEY)
my_df.create_image_index(index_name=gee.NDVI_INDEX, clip_image=True)
my_df.export_to_drive(export_name=None, scale_m2_px=1000)
