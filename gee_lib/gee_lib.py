import ee

# Try to Initialize Earth Engine API and if it fails Authentication is needed first.
try:
    ee.Initialize()
except:
    ee.Authenticate()
    ee.Initialize()

# -------------------------------------- #
# ---------- Table of Context ---------- #
# -------------------------------------- #
'''
1. Create Internal Variables
2. Create Variables
3. Create Internal Functions
4. Create Functions
5. Class
'''
# -------------------------------------- #

# -------------------------------------------------- #
# ---------- 1. Create Internal Variables ---------- #
# -------------------------------------------------- #

_DATE_KEY = 'DATE'
_START_DATE_KEY = 'START_DATE'
_END_DATE_KEY = 'END_DATE'

_GEOMETRY_COUNTRY_COLLECTION = ee.FeatureCollection('users/midekisa/Countries')  # add countries boundary geometries

# ----------------------------------------- #
# ---------- 2. Create Variables ---------- #
# ----------------------------------------- #

'''
-----------------------------------
--- Dataset Acronyms Dictionary ---
-----------------------------------
--- A. ---
AER_AI = AERosol Index
AM     = Atmosphere Monthly
AMGP   = Atmosphere Monthly Global Product
AR     = Agjusted Reflectance
-----------------------------------
--- B. ---
BAI  = Burn Area Index
BAM  = Burned Area Monthly
BRDF = Bidirectional Reflectance Distribution Function
-----------------------------------
--- C. ---
CAMS = Copernicus Atmosphere Monitoring Services
CO = Carbon Monoxide
-----------------------------------
--- D. ---
DS   = DataSet
-----------------------------------
--- E. ---
EFR  = Earth observation Full Resolution 
EVI  = Enchanced Vegetation Index
-----------------------------------
--- F. ---
FPAR = Fraction of Photosynthetically Active Radiation
-----------------------------------
--- G. ---
GRD = Ground Range Detected
GPP = Gross Primary Productivity
GSV = Global Static Variable
-----------------------------------
--- H. ---
HCHO = Formaldehyde
-----------------------------------
--- I. ---
-----------------------------------
--- J. ---
-----------------------------------
--- K. ---
-----------------------------------
--- L. ---
LAI  = Leaf Area Index
LCT  = Land Cover Type
LSTE = Land Surface Temperature and Emissivity
LWMD = Land Water Mask Derived
-----------------------------------
--- M. ---
MP  = Model Parameters
MSI = MultiSpectral Instrument
-----------------------------------
--- N. ---
NBRT = Normalized Burn Ratio Thermal
NCAR = National Center for Atmospheric Research
NCEP = National Centers for Environmental Prediction
NDSI = Normalized Difference Snow Index
NDVI = Normalized Difference Vegetation Index
NDWI = Normalized Difference Water Index
NE   = Net Evapotranspiration
NO2  = Nitroxen Dioxide
NPP  = Net Primary Production
NRT  = Near_Real_Time
-----------------------------------
--- O. ---
O3   = Ozone
OFFL = OFFLine
OLCI = Ocean and Land Color Instrument
OR   = Ocean Reflectance
-----------------------------------
--- P. ---
POI  = Public Ortho Imagery
-----------------------------------
--- Q. ---
-----------------------------------
--- R. ---
RAW    = RAW images
RD  = Reabalysis Data
-----------------------------------
--- S. ---
SAR  = Synthetic Aperture Radar
SC   = Snow Cover
SO2  = Sulphur Dioxide 
SR   = Surface Reflection
-----------------------------------
--- T. ---
TAF  = Thermal Anomalies and Fire
TOA  = Top Of Atmosphere
TOMS = Total Ozone Mapping Spectometer
-----------------------------------
--- U. ---
-----------------------------------
--- V. ---
VI = Vegetation Indices
-----------------------------------
--- W. ---
-----------------------------------
--- X. ---
-----------------------------------
--- Y. ---
-----------------------------------
--- Z. ---
-----------------------------------
'''

# ----- SATELITE BANDS ----- #

GSV_DS_BAND_RED = "RED"
GSV_DS_BAND_BLUE = "BLUE"
GSV_DS_BAND_GREEN = "GREEN"
GSV_DS_BAND_NEAR_INFRARED = "NIR"
GSV_DS_BAND_SHORTWAVE_INFRARED_1 = "SWIR_1"
GSV_DS_BAND_SHORTWAVE_INFRARED_2 = "SWIR_2"
GSV_DS_BAND_THERMAL = "THERMAL"
GSV_DS_BAND_BRIGHTMESS_TEMPERATURE = "BRIGHTNES_TEMPERATURE"
GSV_DS_BAND_ATMOSPHERIC_OPACITY = "ATMOSHPERIC_OPACITY"
GSV_DS_BAND_CLOUD_QA = "CLOUD_QA"
GSV_DS_BAND_PIXEL_QA = "PIXEL_QA"
GSV_DS_BAND_RADSAT_QA = "RADSAT_QA"
GSV_DS_BAND_LANDSAT_BQA = "LANDSAT_BQA"

# ----- LANDSAT DATASETS ----- #

GSV_DS_LANDSAT_1_COLLECTION_ID = 'LANDSAT/LM01/C01/T1'
GSV_DS_LANDSAT_1_DEFAULT_DATE_RANGE = ['1972-07-23T00:00:00', '1978-01-07T00:00:00']
GSV_DS_LANDSAT_2_COLLECTION_ID = 'LANDSAT/LM02/C01/T1'
GSV_DS_LANDSAT_3_COLLECTION_ID = 'LANDSAT/LM03/C01/T1'
GSV_DS_LANDSAT_4_COLLECTION_ID = 'LANDSAT/LM04/C01/T1'
GSV_DS_LANDSAT_5_COLLECTION_ID = 'LANDSAT/LM05/C01/T1'
GSV_DS_LANDSAT_7_COLLECTION_ID = 'LANDSAT/LM07/C01/T1'
GSV_DS_LANDSAT_8_COLLECTION_ID = 'LANDSAT/LM08/C01/T1'

GSV_DS_LANDSAT_4_SR_COLLECTION_ID = "LANDSAT/LT04/C01/T1_SR"
GSV_DS_LANDSAT_4_TOA_COLLECTION_ID = "LANDSAT/LT04/C01/T1_TOA"
GSV_DS_LANDSAT_4_LT_RAW_COLLECTION_ID = "LANDSAT/LT04/C01/T1"

GSV_DS_LANDSAT_4_8DAY_BAI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_4_8DAY_EVI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_4_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_4_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_4_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_4_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDWI"

GSV_DS_LANDSAT_5_SR_COLLECTION_ID = "LANDSAT/LT05/C01/T1_SR"
GSV_DS_LANDSAT_5_TOA_COLLECTION_ID = "LANDSAT/LT05/C01/T1_TOA"
GSV_DS_LANDSAT_5_LT_RAW_COLLECTION_ID = "LANDSAT/LT05/C01/T1"

GSV_DS_LANDSAT_5_8DAY_BAI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_5_8DAY_EVI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_5_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_5_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_5_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_5_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDWI"

GSV_DS_LANDSAT_7_SR_COLLECTION_ID = "LANDSAT/LE07/C01/T1_SR"
GSV_DS_LANDSAT_7_TOA_COLLECTION_ID = "LANDSAT/LE07/C01/T1_TOA"
GSV_DS_LANDSAT_7_LT_RAW_COLLECTION_ID = "LANDSAT/LE07/C01/T1"

GSV_DS_LANDSAT_7_8DAY_BAI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_7_8DAY_EVI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_7_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_7_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_7_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_7_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDWI"

# ----- SENTINEL DATASETS ----- #

GSV_DS_SENTINEL_1_SAR_GRD_COLLECTION_ID = "COPERNICUS/S1_GRD"

GSV_DS_SENTINEL_2_MSI_TOA_COLLECTION_ID = "COPERNICUS/S2"
GSV_DS_SENTINEL_2_MSI_SR_COLLECTION_ID = "COPERNICUS/S2_SR"

GSV_DS_SENTINEL_3_OLCI_EFR_COLLECTION_ID = "COPERNICUS/S3/OLCI"

GSV_DS_SENTINEL_5_OFFL_AER_AI_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_AER_AI"
GSV_DS_SENTINEL_5_OFFL_CLOUD_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CLOUD"
GSV_DS_SENTINEL_5_OFFL_CO_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CO"
GSV_DS_SENTINEL_5_OFFL_HCHO_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_HCHO"
GSV_DS_SENTINEL_5_OFFL_NO2_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_NO2"
GSV_DS_SENTINEL_5_OFFL_O3_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_O3"
GSV_DS_SENTINEL_5_OFFL_SO2_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_SO2"
GSV_DS_SENTINEL_5_OFFL_CH4_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CH4"

# ----- MODIS DATASETS ----- #

GSV_DS_MODIS_NADIR_BRDF_AR_DAILY_500_COLLECTION_ID = "MODIS/006/MCD43A4"
GSV_DS_MODIS_ALBEDO_DAILY_QUALITY_500_COLLECTION_ID = "MODIS/006/MCD43A3"
GSV_DS_MODIS_BRDF_ALBEDO_DAILY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD43A2"
GSV_DS_MODIS_TERRA_SR_DAILY_250_COLLECTION_ID = "MODIS/006/MOD09GQ"
GSV_DS_MODIS_TERRA_SC_DAILY_500_COLLECTION_ID = "MODIS/006/MOD10A1"
GSV_DS_MODIS_TERRA_LSTE_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD11A1"
GSV_DS_MODIS_TERRA_SR_DAILY_GLOBAL_1000_500_COLLECTION_ID = "MODIS/006/MOD09GA"
GSV_DS_MODIS_TERRA_OR_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MODOCGA"
GSV_DS_MODIS_TERRA_TAF_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD14A1"
GSV_DS_MODIS_BRDF_ALBEDO_MP_DAILY_500_COLLECTION_ID = "MODIS/006/MCD43A1"
GSV_DS_MODIS_LAI_FPAR_4_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD15A3H"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD09Q1"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD09A1"
GSV_DS_MODIS_TERRA_LSTE_8_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD11A2"
GSV_DS_MODIS_TERRA_TAF_8_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD14A2"
GSV_DS_MODIS_TERRA_GPP_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD17A2H"
GSV_DS_MODIS_TERRA_NT_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD16A2"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD13Q1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD13A1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD13A2"
GSV_DS_MODIS_BAM_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD64A1"
GSV_DS_MODIS_TERRA_AM_GLOBAL_PRODUCT_COLLECTION_ID = "MODIS/006/MOD08_M3"
GSV_DS_MODIS_LCT_YEARLY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD12Q1"
GSV_DS_MODIS_TERRA_NPP_YEARLY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD17A3H"
GSV_DS_MODIS_TERRA_LWMD_SRTM_YEARLY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD44W"

# ----- HIGH RESOLUTION IMAGERY ----- #

GSV_DS_PLANET_SKYSAT_POI_MULTISPECTRAL_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/MULTISPECTRAL"
GSV_DS_PLANET_SKYSAT_POI_RGB_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"
GSV_DS_NATIONAL_AGRICULTURE_IMAGERY_PROGRAM_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"

# ----- ATMOSPHERIC ----- #

GSV_DS_CAMS_CLOBAL_NRT_COLLECTION_ID = "ECMWF/CAMS/NRT"
GSV_DS_MOD08_M3061_TERRA_AMGP_COLLECTION_ID = "MODIS/061/MOD08_M3"
GSV_DS_MYD08_M3061_AQUA_AMGP_COLLECTION_ID = "MODIS/061/MYD08_M3"
GSV_DS_NCEP_NCAR_RD_SEA_LEVEL_PRESSUR_COLLECTION_ID = "NCEP_RE/sea_level_pressure"
GSV_DS_NCEP_NCAR_RD_SURFACE_TEMPERATURE_COLLECTION_ID = "NCEP_RE/surface_temp"
GSV_DS_NCEP_NCAR_RD_WATER_VAPOR_COLLECTION_ID = "NCEP_RE/surface_wv"
GSV_DS_TOMS_OMI_MERGED_OZONE_DATA_COLLECTION_ID = "TOMS/MERGED"

dict_full_dataset = {
    GSV_DS_LANDSAT_1_COLLECTION_ID: {
        _DATE_KEY: {
            _START_DATE_KEY: GSV_DS_LANDSAT_1_DEFAULT_DATE_RANGE[0],
            _END_DATE_KEY: GSV_DS_LANDSAT_1_DEFAULT_DATE_RANGE[1]
        }
    }
}


# -------------------------------------------------- #
# ---------- 3. Create Internal Functions ---------- #
# -------------------------------------------------- #

# ----------------------------------------- #
# ---------- 4. Create Functions ---------- #
# ----------------------------------------- #

# ------------------------------ #
# ---------- 5. Class ---------- #
# ------------------------------ #


class GoogleEarthEngine:
    """
    This Class will be the core routine
    """

    def __init__(self):
        self._image_collection = None
        self._collection_date_range = None
        self._collection_bounds_geometry = None
        self._image = None

    # ----- Print Functions (Debugging) ----- #

    def prt_image_collection(self):
        print(self._image_collection)

    def prt_date_range(self):
        print(self._collection_date_range)

    def prt_image_geometry(self):
        print(self._collection_bounds_geometry)

    # ----- Core Functions ----- #

    def set_collection_date_range(self, date_range: []):
        self._collection_date_range = date_range

    def set_collection_geometry_from_gee_country_str(self, country: str):
        # Simple create a geometry from GEE country list
        self._collection_bounds_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', country))
        self._collection_bounds_geometry = self._collection_bounds_geometry.geometry()

    def set_collection_geometry_from_gee_country_list(self, list_country: []):
        new_geometry = None  # Create a temporary tmp geometry

        for index in range(0, len(list_country)):
            if index == 0:
                new_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', list_country[index]))
                new_geometry = new_geometry
            else:
                tmp_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', list_country[index]))
                tmp_geometry = tmp_geometry
                new_geometry.merge(tmp_geometry)

        self._collection_bounds_geometry = new_geometry.geometry()

    def set_collection(self, collection_id):
        # Check if user has not specify either a date or a geometry
        if self._collection_date_range is None and self._collection_bounds_geometry is None:
            self._image_collection = ee.ImageCollection(collection_id)  # use only the collection id
        else:  # Else
            start_date = None  # create a start_date variable
            end_date = None  # create an end_date variable
            if self._collection_date_range is None:  # Check if date_range is None
                if collection_id in dict_full_dataset.keys():  # Check if collection ID is in dict keys
                    start_date = dict_full_dataset[collection_id][_DATE_KEY][_START_DATE_KEY]  # use the dict start date
                    end_date = dict_full_dataset[collection_id][_DATE_KEY][_END_DATE_KEY]  # use the dict end date

            if start_date is None and end_date is None:  # if start date continue to be None
                # Filter only by geometry
                self._image_collection = ee.ImageCollection(collection_id).filterBounds(
                    self._collection_bounds_geometry)
            else:
                if self._collection_bounds_geometry is None:  # if geometry is None
                    self._image_collection = ee.ImageCollection(collection_id).filterDate(start_date, end_date)
                else:  # Else
                    self._image_collection = ee.ImageCollection(collection_id).filterDate(start_date,
                                                                                          end_date).filterBounds(
                        self._collection_bounds_geometry)

    def create_image_form_collection_mean(self):
        self._image = self._image_collection.select(['B4']).mean().clip(self._collection_bounds_geometry)
        print(self._image)

    def export_to_Drive(self):
        task_bash = {
            'image': self._image,
            'description': "something",
            'region': self._collection_bounds_geometry,
            'scale': 10000,
            'folder': 'GEE_TEST'
        }
        task = ee.batch.Export.image.toDrive(**task_bash)
        task.start()
