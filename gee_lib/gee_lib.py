import ee

# Try to Initialize Earth Engine API and if it fails Authentication is needed first.
try:
    ee.Initialize()
except:
    ee.Authenticate()
    ee.Initialize()

# -------------------------------------------------------- #
# ---------- Table of Context and Abbreviations ---------- #
# -------------------------------------------------------- #
'''
1. Create Internal Variables
2. Create Variables
3. Create Internal Functions
4. Create Functions
5. Class
'''
# -------------------------------------- #

'''
-----------------------------------
---------- Abbreviations ----------
-----------------------------------
--- A. ---
AER_AI = AERosol Index
AM     = Atmosphere Monthly
AMF    = Air Mass Factor
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
NBR  = Normalized Burn Ratio
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

# -------------------------------------------------- #
# ---------- 1. Create Internal Variables ---------- #
# -------------------------------------------------- #

_COLLECTION_ID_DKEY = 'COLLECTION_ID'
_DATE_DKEY = 'DATE'
_START_DATE_DKEY = 'START_DATE'
_END_DATE_DKEY = 'END_DATE'
_BANDS_DKEY = 'BANDS'

# ----- SATELITE BANDS ----- #

_SINGLE_BAND_DKEY = 'SINGLE_BAND'
_RED_DKEY = 'RED'
_GREEN_DKEY = 'GREEN'
_BLUE_DKEY = 'BLUE'
_NIR_DKEY = 'NIR'
_NIR_1_DKEY = 'NIR_1'
_NIR_2_DKEY = 'NIR_2'
_SWIR_1_DKEY = 'SWIR_1'
_SWIR_2_DKEY = 'SWIR_2'
_BQA_DKEY = 'BQA'
_THERMAL_INFRARED_DKEY = 'THERMAL_INFRARED'
_BRIGHTNESS_TEMPERATURE_1_DKEY = 'BRIGHTNESS_TEMPERATURE_1'
_BRIGHTNESS_TEMPERATURE_2_DKEY = 'BRIGHTNESS_TEMPERATURE_2'
_THERMAL_INFRARED_1_DKEY = 'THERMAL_INFRARED_1'
_THERMAL_INFRARED_2_DKEY = 'THERMAL_INFRARED_2'
_PANCHROMATIC_DKEY = 'PANCHROMATIC'
_ULTRA_BLUE_DKEY = 'ULTRA_BLUE'
_COASTAL_AEROSOL_DKEY = 'COASTAL_AEROSOL'
_CIRRUS_DKEY = 'CIRRUS'
_HH_DKEY = 'HH'
_HV_DKEY = 'HV'
_VV_DKEY = 'VV'
_VH_DKEY = 'VH'
_AEROSOL_DKEY = 'AEROSOL'
_RED_EDGE_1_DKEY = 'RED_EDGE_1'
_RED_EDGE_2_DKEY = 'RED_EDGE_2'
_RED_EDGE_3_DKEY = 'RED_EDGE_3'
_RED_EDGE_4_DKEY = 'RED_EDGE_4'
_WATER_VAPOR_DKEY = 'WATER_VAPOR'

_S03_AEROSOL_CORRECTION_DKEY = 'AEROSOL_CORRECTION'
_S03_YELLOW_SUBSTANCE_DKEY = 'YELLOW_SUBSTANCE'
_S03_CHL_ABSORPTION_MAX_DKEY = 'CHL_ABSORPTION_MAX'
_S03_HIGH_CHL_DKEY = 'HIGH_CHL'
_S03_CHL_SEDIMENT_TURBIDITY_RED_TIDE_DKEY = 'CHL_SEDIMENT_TURBIDITY_RED_TIDE'
_S03_CHLOROPHYLL_REFERENCE_DKEY = 'CHOROPHYLL_REFERENCE'
_S03_SEDIMENT_LOADING_DKEY = 'SEDIMENT_LOADING'
_S03_CHL_SEDIMENT_YELLOW_SUBSTANCE_VEGETATION_DKEY = 'CHL_SEDIMENT_YELLOW_SUBSTANCE_VEGETATION'
_S03_FLUORESCENCE_RETRIEVAL_DKEY = 'FLUORESCENCE_RETRIEVAL'
_S03_CHL_FLUORESCENCE_PEAK_RED_EDGE_DKEY = 'CHL_FLUORESCENCE_PEAK_RED_EDGE'
_S03_CHL_FLUORESCENCE_BASELINE_RED_EDGE_TRANSITION_DKEY = 'CHL_FLUORESCENCE_BASELINE_RED_EDGE_TRANSITION'
_S03_O2_ABSORPTION_CLOUDS_VEGETATION_DKEY = 'O2_ABSORPTION_CLOUDS_VEGETATION'
_S03_O2_ABSORPTION_AEROSOL_CORRECTION_DKEY = 'O2_ABSORPTION_AEROSOL_CORRECTION'
_S03_ATMOSPHERIC_CORRECTION_DKEY = 'ATMOSPHERIC_CORRECTION'
_S03_O2A_FOR_CLOUD_TOP_PRESSURE_FLUORESCENCE_OVER_LAND_DKEY = 'O2A_FOR_CLOUD_TOP_PRESSURE_FLUORESCENCE_OVER_LAND'
_S03_ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION_DKEY = 'ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION'
_S03_ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION_CLOUDS_PX_COREGUSTRATION_DKEY = 'ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION_CLOUDS_PX_COREGUSTRATION'
_S03_VEGETATION_MONITORING_DKEY = 'VEGETATION_MONITORING'
_S03_WATER_VAPOUR_ABSORPTION_VEGETATION_MONITORING_DKEY = 'WATER_VAPOUR_ABSORPTION_VEGETATION_MONITORING'
_S03_WATER_VAPOUR_ABSORPTION_ATMOSPHERIC_AEROSOL_CORRECTION_DKEY = 'WATER_VAPOUR_ABSORPTION_ATMOSPHERIC_AEROSOL_CORRECTION'
_S03_ATMOSPHERIC_AEROSOL_CORRECTION_DKEY = 'ATMOSPHERIC_AEROSOL_CORRECTION'
_S03_QUALITY_FLAGS_DKEY = 'AEROSOL_CORRECTION'

_S05_ABSORBING_AEROSOL_INDEX_DKEY = "ABSORBING_AEROSOL_INDEX"

_S05_CLOUD_TOP_PRESSURE_DKEY = 'CLOUD_TOP_PRESSURE'
_S05_CLOUD_TOP_HEIGHT_DKEY = 'CLOUD_TOP_HEIGHT'
_S05_CLOUD_BASE_PRESSURE_DKEY = 'CLOUD_BASE_PRESSURE'
_S05_CLOUD_BASE_HEIGHT_DKEY = 'CLOUD_BASE_HEIGHT'
_S05_CLOUD_OPTICAL_DEPTH_DKEY = 'CLOUD_OPTICAL_DEPTH'
_S05_SURFACE_ALBEDO_DKEY = 'SURFACE_ALBEDO'

_S05_CO_COLUMN_NUMBER_DENSITY_DKEY = 'CO_COLUMN_NUMBER_DENSITY'
_S05_H20_COLUMN_NUMBER_DENSITY_DKEY = 'H20_COLUMN_NUMBER_DENSITY'
_S05_CLOUD_HEIGHT_DKEY = 'CLOUD_HEIGHT'

_S05_TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY_DKEY = 'TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY'
_S05_TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY_AMF_DKEY = 'TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY_AMF'
_S05_HCHO_SLANT_COLUMN_NUMBER_DENSITY_DKEY = 'HCHO_SLANT_COLUMN_NUMBER_DENSITY'

_S05_NO2_COLUMN_NUMBER_DENSITY_DKEY = 'NO2_COLUMN_NUMBER_DENSITY'
_S05_TROPOSPHERIC_NO2_COLUMN_NUMBER_DENSITY_DKEY = 'TROPOSPHERIC_NO2_COLUMN_NUMBER_DENSITY'
_S05_STRATOSPHERIC_NO2_COLUMN_NUMBER_DENSITY_DKEY = 'STRATOSPHERIC_NO2_COLUMN_NUMBER_DENSITY'
_S05_NO2_SLANT_COLUMN_NUMBER_DENSITY_DKEY = 'NO2_SLANT_COLUMN_NUMBER_DENSITY'
_S05_TROPOPAUSE_PRESSURE_DKEY = 'TROPOPAUSE_PRESSURE'

_S05_O3_COLUMN_NUMBER_DENSITY_DKEY = 'O3_COLUMN_NUMBER_DENSITY'
_S05_O3_EFFECTIVE_TEMPERATURE_DKEY = 'O3_EFFECTIVE_TEMPERATURE'

_S05_S02_COLUMN_NUMBER_DENSITY_DKEY = 'S02_COLUMN_NUMBER_DENSITY'
_S05_S02_COLUMN_NUMBER_DENSITY_AMF_DKEY = 'S02_COLUMN_NUMBER_DENSITY_AMF'
_S05_S02_SLANT_COLUMN_NUMBER_DENSITY_DKEY = 'S02_SLANT_COLUMN_NUMBER_DENSITY'
_S05_S02_COLUMN_NUMBER_DENSITY_15KM_DKEY = 'S02_COLUMN_NUMBER_DENSITY_15KM'

_S05_CH4_COLUMN_VOLUME_MIXING_RATIO_DRY_AIR_DKEY = 'CH4_COLUMN_VOLUME_MIXING_RATIO_DRY_AIR'
_S05_AEROSOL_HEIGHT_DKEY = 'AEROSOL_HEIGHT'
_S05_AEROSOL_OPTICAL_DEPTH_DKEY = 'AEROSOL_OPTICAL_DEPTH'

_S05_CLOUD_FRACTION_DKEY = 'CLOUD_FRACTION'
_S05_SENSOR_ALTITUDE_DKEY = 'SENSOR_ALTITUDE'
_S05_SENSOR_AZIMUTH_ANGLE_DKEY = 'SENSOR_AZIMUTH_ANGLE'
_S05_SENSOR_ZENITH_ANGLE_DKEY = 'SENSOR_ZENITH_ANGLE'
_S05_SOLAR_AZIMUTH_ANGLE_DKEY = 'SOLAR_AZIMUTH_ANGLE'
_S05_SOLAR_ZENITH_ANGLE_DKEY = 'SOLAR_ZENITH_ANGLE'


# ----- Google Earth Engine Country Shapefiles ----- #

_GEOMETRY_COUNTRY_COLLECTION = ee.FeatureCollection('users/midekisa/Countries')  # add countries boundary geometries


# ----------------------------------------- #
# ---------- 2. Create Variables ---------- #
# ----------------------------------------- #

# ----- LANDSAT DATASETS ----- #

GSV_DS_LANDSAT_1_T1_DKEY = "LANDSAT_1_T1"
GSV_DS_LANDSAT_2_T1_DKEY = "LANDSAT_2_T1"
GSV_DS_LANDSAT_3_T1_DKEY = "LANDSAT_3_T1"

GSV_DS_LANDSAT_4_T1_DKEY = "LANDSAT_4_T1"
GSV_DS_LANDSAT_4_SR_T1_DKEY = "LANDSAT_4_SR_T1"
GSV_DS_LANDSAT_4_TOA_T1_DKEY = "LANDSAT_4_TOA_T1"
GSV_DS_LANDSAT_4_RAW_T1_DKEY = "LANDSAT_4_RAW_T1"
GSV_DS_LANDSAT_4_8DAY_BAI_DKEY = "LANDSAT_4_8DAY_BAI_T1"
GSV_DS_LANDSAT_4_8DAY_EVI_DKEY = "LANDSAT_4_8DAY_EVI_T1"
GSV_DS_LANDSAT_4_8DAY_NDVI_DKEY = "LANDSAT_4_8DAY_NDVI_T1"
GSV_DS_LANDSAT_4_8DAY_NBRT_DKEY = "LANDSAT_4_8DAY_NBRT_T1"
GSV_DS_LANDSAT_4_8DAY_NDSI_DKEY = "LANDSAT_4_8DAY_NDSI_T1"
GSV_DS_LANDSAT_4_8DAY_NDWI_DKEY = "LANDSAT_4_8DAY_NDWI_T1"

GSV_DS_LANDSAT_5_DKEY = "LANDSAT_5"
GSV_DS_LANDSAT_5_SR_T1_DKEY = "LANDSAT_5_SR_T1"
GSV_DS_LANDSAT_5_TOA_T1_DKEY = "LANDSAT_5_TOA_T1"
GSV_DS_LANDSAT_5_RAW_T1_DKEY = "LANDSAT_5_RAW_T1"
GSV_DS_LANDSAT_5_8DAY_BAI_DKEY = "LANDSAT_5_8DAY_BAI_T1"
GSV_DS_LANDSAT_5_8DAY_EVI_DKEY = "LANDSAT_5_8DAY_EVI_T1"
GSV_DS_LANDSAT_5_8DAY_NDVI_DKEY = "LANDSAT_5_8DAY_NDVI_T1"
GSV_DS_LANDSAT_5_8DAY_NBRT_DKEY = "LANDSAT_5_8DAY_NBRT_T1"
GSV_DS_LANDSAT_5_8DAY_NDSI_DKEY = "LANDSAT_5_8DAY_NDSI_T1"
GSV_DS_LANDSAT_5_8DAY_NDWI_DKEY = "LANDSAT_5_8DAY_NDWI_T1"

GSV_DS_LANDSAT_7_SR_T1_DKEY = "LANDSAT_7_SR_T1"
GSV_DS_LANDSAT_7_TOA_T1_DKEY = "LANDSAT_7_TOA_T1"
GSV_DS_LANDSAT_7_RAW_T1_DKEY = "LANDSAT_7_RAW_T1"
GSV_DS_LANDSAT_7_8DAY_BAI_DKEY = "LANDSAT_7_8DAY_BAI_T1"
GSV_DS_LANDSAT_7_8DAY_EVI_DKEY = "LANDSAT_7_8DAY_EVI_T1"
GSV_DS_LANDSAT_7_8DAY_NDVI_DKEY = "LANDSAT_7_8DAY_NDVI_T1"
GSV_DS_LANDSAT_7_8DAY_NBRT_DKEY = "LANDSAT_7_8DAY_NBRT_T1"
GSV_DS_LANDSAT_7_8DAY_NDSI_DKEY = "LANDSAT_7_8DAY_NDSI_T1"
GSV_DS_LANDSAT_7_8DAY_NDWI_DKEY = "LANDSAT_7_8DAY_NDWI_T1"

GSV_DS_LANDSAT_8_SR_T1_DKEY = "LANDSAT_8_SR_T1"
GSV_DS_LANDSAT_8_TOA_T1_DKEY = "LANDSAT_8_TOA_T1"
GSV_DS_LANDSAT_8_RAW_T1_DKEY = "LANDSAT_8_RAW_T1"
GSV_DS_LANDSAT_8_8DAY_BAI_DKEY = "LANDSAT_8_8DAY_BAI_T1"
GSV_DS_LANDSAT_8_8DAY_EVI_DKEY = "LANDSAT_8_8DAY_EVI_T1"
GSV_DS_LANDSAT_8_8DAY_NDVI_DKEY = "LANDSAT_8_8DAY_NDVI_T1"
GSV_DS_LANDSAT_8_8DAY_NBRT_DKEY = "LANDSAT_8_8DAY_NBRT_T1"
GSV_DS_LANDSAT_8_8DAY_NDSI_DKEY = "LANDSAT_8_8DAY_NDSI_T1"
GSV_DS_LANDSAT_8_8DAY_NDWI_DKEY = "LANDSAT_8_8DAY_NDWI_T1"

# ----- SENTINEL DATASETS ----- #

GSV_DS_SENTINEL_1_SAR_GRD_DKEY = "SENTINEL_1_SAR_GRD"

GSV_DS_SENTINEL_2_MSI_TOA_DKEY = "SENTINEL_2_MSI_TOA"
GSV_DS_SENTINEL_2_MSI_SR_DKEY = "SENTINEL_2_MSI_SR"

GSV_DS_SENTINEL_3_OLCI_EFR_DKEY = "SENTINEL_3_OLCI_EFR"

GSV_DS_SENTINEL_5_OFFL_AER_AI_DKEY = "SENTINEL_5_OFFLINE_AEROSOL_AI"
GSV_DS_SENTINEL_5_OFFL_CLOUD_DKEY = "SENTINEL_5_OFFLINE_CLOUD"
GSV_DS_SENTINEL_5_OFFL_CO_DKEY = "SENTINEL_5_OFFLINE_CARBON_MONOXIDE"
GSV_DS_SENTINEL_5_OFFL_HCHO_DKEY = "SENTINEL_5_OFFLINE_FORMALDEHYDE"
GSV_DS_SENTINEL_5_OFFL_NO2_DKEY = "SENTINEL_5_OFFLINE_NITROGEN_DIOXIDE"
GSV_DS_SENTINEL_5_OFFL_O3_DKEY = "SENTINEL_5_OFFLINE_OZONE"
GSV_DS_SENTINEL_5_OFFL_SO2_DKEY = "SENTINEL_5_OFFLINE_SULPHUR_DIOXIDE"
GSV_DS_SENTINEL_5_OFFL_CH4_DKEY = "SENTINEL_5_OFFLINE_METHANE"

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

# ----- INDEXES ----- #
BAI_INDEX = 'BAI'
EVI_INDEX = 'EVI'
EVI2_INDEX = 'EVI2'
NDVI_INDEX = 'NDVI'
NBR_INDEX = 'NBR'
NBRT_INDEX = 'NBRT'
NDSI_INDEX = 'NDSI'
NDWI_INDEX = 'NDWI'

PX_BASE_MIN = 'MIN'
PX_BASE_MAX = 'MAX'
PX_BASE_MEAN = 'MEAN'

# ----- DICTIONARY DATASET ----- #

DICT_FULL_DATASET = {
    GSV_DS_LANDSAT_1_T1_DKEY: {  # LANDSAT 1 DATASET
        _COLLECTION_ID_DKEY: 'LANDSAT/LM01/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1972-07-23T00:00:00',
            _END_DATE_DKEY: '1978-01-07T00:00:00'
        },
        _BANDS_DKEY: {
            _GREEN_DKEY: 'B4',
            _RED_DKEY: 'B5',
            _NIR_1_DKEY: 'B6',
            _NIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_2_T1_DKEY: {  # LANDSAT 2 DATASET
        _COLLECTION_ID_DKEY: 'LANDSAT/LM02/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1975-01-22T00:00:00',
            _END_DATE_DKEY: '1982-02-26T00:00:00'
        },
        _BANDS_DKEY: {
            _GREEN_DKEY: 'B4',
            _RED_DKEY: 'B5',
            _NIR_1_DKEY: 'B6',
            _NIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_3_T1_DKEY: {  # LANDSAT 3 DATASET
        _COLLECTION_ID_DKEY: 'LANDSAT/LM03/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1978-03-05T00:00:00',
            _END_DATE_DKEY: '1983-03-31T00:00:00'
        },
        _BANDS_DKEY: {
            _GREEN_DKEY: 'B4',
            _RED_DKEY: 'B5',
            _NIR_1_DKEY: 'B6',
            _NIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_T1_DKEY: {  # LANDSAT 4 DATASET
        _COLLECTION_ID_DKEY: 'LANDSAT/LM04/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1982-07-16T00:00:00',
            _END_DATE_DKEY: '1993-12-14T00:00:00'
        },
        _BANDS_DKEY: {
            _GREEN_DKEY: 'B4',
            _RED_DKEY: 'B5',
            _NIR_1_DKEY: 'B6',
            _NIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_SR_T1_DKEY: {  # LANDSAT 4 SR T1
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_SR',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-03-01T00:00:00',
            _END_DATE_DKEY: '2013-01-31T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7'
        }
    }, GSV_DS_LANDSAT_4_TOA_T1_DKEY: {  # LANDSAT 4 SR TOA
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_TOA',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-03-01T00:00:00',
            _END_DATE_DKEY: '2013-01-31T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_RAW_T1_DKEY: {  # LANDSAT 4 RAW
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1982-08-22T00:00:00',
            _END_DATE_DKEY: '1982-08-22T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_8DAY_BAI_DKEY: {  # LANDSAT 4 BAI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_BAI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_EVI_DKEY: {  # LANDSAT 4 EVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_EVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDVI_DKEY: {  # LANDSAT 4 NDVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_NDVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NBRT_DKEY: {  # LANDSAT 4 NBRT
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_NBRT',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDSI_DKEY: {  # LANDSAT 4 NDSI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_NDSI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDWI_DKEY: {  # LANDSAT 4 NDWI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT04/C01/T1_8DAY_NDWI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1989-01-01',
            _END_DATE_DKEY: '1992-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_5_DKEY: {  # LANDSAT 5
        _COLLECTION_ID_DKEY: 'LANDSAT/LM05/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-03-01T00:00:00',
            _END_DATE_DKEY: '2013-01-31T00:00:00'
        },
        _BANDS_DKEY: {
            _GREEN_DKEY: 'B4',
            _RED_DKEY: 'B5',
            _NIR_1_DKEY: 'B6',
            _NIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_SR_T1_DKEY: {  # LANDSAT 5 SR T1
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_SR',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-01-01T00:00:00',
            _END_DATE_DKEY: '2012-05-05T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7'
        }
    }, GSV_DS_LANDSAT_5_TOA_T1_DKEY: {  # LANDSAT 5 SR TOA
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_TOA',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-01-01T00:00:00',
            _END_DATE_DKEY: '2012-05-05T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_RAW_T1_DKEY: {  # LANDSAT 5 RAW
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1984-01-01T00:00:00',
            _END_DATE_DKEY: '2012-05-05T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_8DAY_BAI_DKEY: {  # LANDSAT 5 BAI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_BAI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_EVI_DKEY: {  # LANDSAT 5 EVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_EVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDVI_DKEY: {  # LANDSAT 5 NDVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_NDVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NBRT_DKEY: {  # LANDSAT 5 NBRT
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_NBRT',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDSI_DKEY: {  # LANDSAT 5 NDSI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_NDSI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDWI_DKEY: {  # LANDSAT 5 NDWI
        _COLLECTION_ID_DKEY: 'LANDSAT/LT05/C01/T1_8DAY_NDWI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2011-01-01',
            _END_DATE_DKEY: '2011-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_7_SR_T1_DKEY: {  # LANDSAT 7 SR T1
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_SR',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01T00:00:00',
            _END_DATE_DKEY: '2021-01-13T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7'
        }
    }, GSV_DS_LANDSAT_7_TOA_T1_DKEY: {  # LANDSAT 7 SR TOA
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_TOA',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01T00:00:00',
            _END_DATE_DKEY: '2021-01-15T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_1_DKEY: 'B6_VCID_1',
            _THERMAL_INFRARED_2_DKEY: 'B6_VCID_2',
            _SWIR_2_DKEY: 'B7',
            _PANCHROMATIC_DKEY: 'B8',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_7_RAW_T1_DKEY: {  # LANDSAT 7 RAW
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01T00:00:00',
            _END_DATE_DKEY: '2021-01-15T00:00:00'
        },
        _BANDS_DKEY: {
            _BLUE_DKEY: 'B1',
            _GREEN_DKEY: 'B2',
            _RED_DKEY: 'B3',
            _NIR_DKEY: 'B4',
            _SWIR_1_DKEY: 'B5',
            _THERMAL_INFRARED_1_DKEY: 'B6_VCID_1',
            _THERMAL_INFRARED_2_DKEY: 'B6_VCID_2',
            _SWIR_2_DKEY: 'B7',
            _PANCHROMATIC_DKEY: 'B8',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_7_8DAY_BAI_DKEY: {  # LANDSAT 7 BAI
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_BAI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_EVI_DKEY: {  # LANDSAT 7 EVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_EVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDVI_DKEY: {  # LANDSAT 7 NDVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_NDVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NBRT_DKEY: {  # LANDSAT 7 NBRT
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_NBRT',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDSI_DKEY: {  # LANDSAT 7 NDSI
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_NDSI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDWI_DKEY: {  # LANDSAT 7 NDWI
        _COLLECTION_ID_DKEY: 'LANDSAT/LE07/C01/T1_8DAY_NDWI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01',
            _END_DATE_DKEY: '2002-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_8_SR_T1_DKEY: {  # LANDSAT 8 SR T1
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_SR',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2013-04-11T00:00:00',
            _END_DATE_DKEY: '2021-01-22T00:00:00'
        },
        _BANDS_DKEY: {
            _ULTRA_BLUE_DKEY: 'B1',
            _BLUE_DKEY: 'B2',
            _GREEN_DKEY: 'B3',
            _RED_DKEY: 'B4',
            _NIR_DKEY: 'B5',
            _SWIR_1_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _BRIGHTNESS_TEMPERATURE_1_DKEY: 'B10',
            _BRIGHTNESS_TEMPERATURE_2_DKEY: 'B11'
        }
    }, GSV_DS_LANDSAT_8_TOA_T1_DKEY: {  # LANDSAT 8 SR TOA
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_TOA',
        _DATE_DKEY: {
            _START_DATE_DKEY: '1999-01-01T00:00:00',
            _END_DATE_DKEY: '2021-01-15T00:00:00'
        },
        _BANDS_DKEY: {
            _COASTAL_AEROSOL_DKEY: 'B1',
            _BLUE_DKEY: 'B2',
            _GREEN_DKEY: 'B3',
            _RED_DKEY: 'B4',
            _NIR_DKEY: 'B5',
            _SWIR_1_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _PANCHROMATIC_DKEY: 'B8',
            _CIRRUS_DKEY: 'B9',
            _THERMAL_INFRARED_1_DKEY: 'B10',
            _THERMAL_INFRARED_2_DKEY: 'B11',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_8_RAW_T1_DKEY: {  # LANDSAT 8 RAW
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2013-04-11T00:00:00',
            _END_DATE_DKEY: '2021-02-05T00:00:00'
        },
        _BANDS_DKEY: {
            _COASTAL_AEROSOL_DKEY: 'B1',
            _BLUE_DKEY: 'B2',
            _GREEN_DKEY: 'B3',
            _RED_DKEY: 'B4',
            _NIR_DKEY: 'B5',
            _SWIR_1_DKEY: 'B6',
            _SWIR_2_DKEY: 'B7',
            _PANCHROMATIC_DKEY: 'B8',
            _CIRRUS_DKEY: 'B9',
            _THERMAL_INFRARED_1_DKEY: 'B10',
            _THERMAL_INFRARED_2_DKEY: 'B11',
            _BQA_DKEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_8_8DAY_BAI_DKEY: {  # LANDSAT 8 BAI
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_BAI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_EVI_DKEY: {  # LANDSAT 8 EVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_EVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDVI_DKEY: {  # LANDSAT 8 NDVI
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_NDVI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NBRT_DKEY: {  # LANDSAT 8 NBRT
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_NBRT',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDSI_DKEY: {  # LANDSAT 8 NDSI
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_NDSI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDWI_DKEY: {  # LANDSAT 8 NDWI
        _COLLECTION_ID_DKEY: 'LANDSAT/LC08/C01/T1_8DAY_NDWI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-01-01',
            _END_DATE_DKEY: '2017-12-31'
        },
        _BANDS_DKEY: {
            _SINGLE_BAND_DKEY: 'NDWI'
        }
    }, GSV_DS_SENTINEL_1_SAR_GRD_DKEY: {  # SENTINEL 1 SAR GRD
        _COLLECTION_ID_DKEY: 'COPERNICUS/S1_GRD',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2014-10-03T00:00:00',
            _END_DATE_DKEY: '2021-02-10T00:00:00'
        },
        _BANDS_DKEY: {
            _HH_DKEY: 'HH',
            _HV_DKEY: 'HV',
            _VV_DKEY: 'VV',
            _VH_DKEY: 'VH',
        }
    }, GSV_DS_SENTINEL_2_MSI_TOA_DKEY: {  # SENTINEL 2 MSI TOA
        _COLLECTION_ID_DKEY: 'COPERNICUS/S2',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2015-06-23T00:00:00',
            _END_DATE_DKEY: '2021-02-12T00:00:00'
        },
        _BANDS_DKEY: {
            _AEROSOL_DKEY: 'B1',
            _BLUE_DKEY: 'B2',
            _GREEN_DKEY: 'B3',
            _RED_DKEY: 'B4',
            _RED_EDGE_1_DKEY: 'B5',
            _RED_EDGE_2_DKEY: 'B6',
            _RED_EDGE_3_DKEY: 'B7',
            _NIR_DKEY: 'B8',
            _RED_EDGE_4_DKEY: 'B8A',
            _WATER_VAPOR_DKEY: 'B9',
            _CIRRUS_DKEY: 'B10',
            _SWIR_1_DKEY: 'B11',
            _SWIR_2_DKEY: 'B12'
        }
    }, GSV_DS_SENTINEL_2_MSI_SR_DKEY: {  # SENTINEL 2 MSI SR
        _COLLECTION_ID_DKEY: 'COPERNICUS/S2_SR',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2017-03-28T00:00:00',
            _END_DATE_DKEY: '2021-02-12T00:00:00'
        },
        _BANDS_DKEY: {
            _AEROSOL_DKEY: 'B1',
            _BLUE_DKEY: 'B2',
            _GREEN_DKEY: 'B3',
            _RED_DKEY: 'B4',
            _RED_EDGE_1_DKEY: 'B5',
            _RED_EDGE_2_DKEY: 'B6',
            _RED_EDGE_3_DKEY: 'B7',
            _NIR_DKEY: 'B8',
            _RED_EDGE_4_DKEY: 'B8A',
            _WATER_VAPOR_DKEY: 'B9',
            _CIRRUS_DKEY: 'B10',
            _SWIR_1_DKEY: 'B11',
            _SWIR_2_DKEY: 'B12'
        }
    }, GSV_DS_SENTINEL_3_OLCI_EFR_DKEY: {  # SENTINEL 3 OLCI EFR
        _COLLECTION_ID_DKEY: 'COPERNICUS/S3/OLCI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2016-10-18T19:25:42',
            _END_DATE_DKEY: '2021-02-12T00:00:00'
        },
        _BANDS_DKEY: {
            _S03_AEROSOL_CORRECTION_DKEY: 'Oa01_radiance',
            _S03_YELLOW_SUBSTANCE_DKEY: 'Oa02_radiance',
            _S03_CHL_ABSORPTION_MAX_DKEY: 'Oa03_radiance',
            _S03_HIGH_CHL_DKEY: 'Oa04_radiance',
            _S03_CHL_SEDIMENT_TURBIDITY_RED_TIDE_DKEY: 'Oa05_radiance',
            _S03_CHLOROPHYLL_REFERENCE_DKEY: 'Oa06_radiance',
            _S03_SEDIMENT_LOADING_DKEY: 'Oa07_radiance',
            _S03_CHL_SEDIMENT_YELLOW_SUBSTANCE_VEGETATION_DKEY: 'Oa08_radiance',
            _S03_FLUORESCENCE_RETRIEVAL_DKEY: 'Oa09_radiance',
            _S03_CHL_FLUORESCENCE_PEAK_RED_EDGE_DKEY: 'Oa10_radiance',
            _S03_CHL_FLUORESCENCE_BASELINE_RED_EDGE_TRANSITION_DKEY: 'Oa11_radiance',
            _S03_O2_ABSORPTION_CLOUDS_VEGETATION_DKEY: 'Oa12_radiance',
            _S03_O2_ABSORPTION_AEROSOL_CORRECTION_DKEY: 'Oa13_radiance',
            _S03_ATMOSPHERIC_CORRECTION_DKEY: 'Oa14_radiance',
            _S03_O2A_FOR_CLOUD_TOP_PRESSURE_FLUORESCENCE_OVER_LAND_DKEY: 'Oa15_radiance',
            _S03_ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION_DKEY: 'Oa16_radiance',
            _S03_ATMOSPHERIC_CORRECTION_AEROSOL_CORRECTION_CLOUDS_PX_COREGUSTRATION_DKEY: 'Oa17_radiance',
            _S03_VEGETATION_MONITORING_DKEY: 'Oa18_radiance',
            _S03_WATER_VAPOUR_ABSORPTION_VEGETATION_MONITORING_DKEY: 'Oa19_radiance',
            _S03_WATER_VAPOUR_ABSORPTION_ATMOSPHERIC_AEROSOL_CORRECTION_DKEY: 'Oa20_radiance',
            _S03_ATMOSPHERIC_AEROSOL_CORRECTION_DKEY: 'Oa21_radiance',
            _S03_QUALITY_FLAGS_DKEY: 'quality_flags'
        }
    }, GSV_DS_SENTINEL_5_OFFL_AER_AI_DKEY: {  # SENTINEL 5 AER AI
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_AER_AI',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-07-04T13:34:21',
            _END_DATE_DKEY: '2021-02-11T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_ABSORBING_AEROSOL_INDEX_DKEY: 'absorbing_aerosol_index',
            _S05_SENSOR_ALTITUDE_DKEY: 'sensor_altitude',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_CLOUD_DKEY: {  # SENTINEL 5 CLOUD
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_CLOUD',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-07-04T11:34:21',
            _END_DATE_DKEY: '2021-02-11T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_CLOUD_FRACTION_DKEY: 'cloud_fraction',
            _S05_CLOUD_TOP_PRESSURE_DKEY: 'cloud_top_pressure',
            _S05_CLOUD_TOP_HEIGHT_DKEY: 'cloud_top_height',
            _S05_CLOUD_BASE_PRESSURE_DKEY: 'cloud_base_pressure',
            _S05_CLOUD_BASE_HEIGHT_DKEY: 'cloud_base_height',
            _S05_CLOUD_OPTICAL_DEPTH_DKEY: 'cloud_optical_depth',
            _S05_SURFACE_ALBEDO_DKEY: 'surface_albedo',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_CO_DKEY: {  # SENTINEL 5 CO
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_CO',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-06-28T10:24:07',
            _END_DATE_DKEY: '2021-02-11T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_CO_COLUMN_NUMBER_DENSITY_DKEY: 'CO_column_number_density',
            _S05_H20_COLUMN_NUMBER_DENSITY_DKEY: 'H2O_column_number_density',
            _S05_CLOUD_HEIGHT_DKEY: 'cloud_height',
            _S05_SENSOR_ALTITUDE_DKEY: 'sensor_altitude',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_HCHO_DKEY: {  # SENTINEL 5 HCHO
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_HCHO',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-12-05T12:14:36',
            _END_DATE_DKEY: '2021-02-11T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY_DKEY: 'tropospheric_HCHO_column_number_density',
            _S05_TROPOSHERIC_HCHO_COLUMN_NUMBER_DENSITY_AMF_DKEY: 'tropospheric_HCHO_column_number_density_amf',
            _S05_HCHO_SLANT_COLUMN_NUMBER_DENSITY_DKEY: 'HCHO_slant_column_number_density',
            _S05_CLOUD_FRACTION_DKEY: 'cloud_fraction',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_NO2_DKEY: {  # SENTINEL 5 NO2
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_NO2',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-06-28T10:24:07',
            _END_DATE_DKEY: '2021-02-03T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_NO2_COLUMN_NUMBER_DENSITY_DKEY: 'NO2_column_number_density',
            _S05_TROPOSPHERIC_NO2_COLUMN_NUMBER_DENSITY_DKEY: 'tropospheric_NO2_column_number_density',
            _S05_STRATOSPHERIC_NO2_COLUMN_NUMBER_DENSITY_DKEY: 'stratospheric_NO2_column_number_density',
            _S05_NO2_SLANT_COLUMN_NUMBER_DENSITY_DKEY: 'NO2_slant_column_number_density',
            _S05_TROPOPAUSE_PRESSURE_DKEY: 'tropopause_pressure',
            _S05_ABSORBING_AEROSOL_INDEX_DKEY: 'absorbing_aerosol_index',
            _S05_CLOUD_FRACTION_DKEY: 'cloud_fraction',
            _S05_SENSOR_ALTITUDE_DKEY: 'sensor_altitude',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_O3_DKEY: {  # SENTINEL 5 O3
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_O3',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-09-08T21:19:29',
            _END_DATE_DKEY: '2021-02-10T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_O3_COLUMN_NUMBER_DENSITY_DKEY: 'O3_column_number_density',
            _S05_O3_EFFECTIVE_TEMPERATURE_DKEY: 'O3_effective_temperature',
            _S05_CLOUD_FRACTION_DKEY: 'cloud_fraction',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    }, GSV_DS_SENTINEL_5_OFFL_SO2_DKEY: {  # SENTINEL 5 SO2
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_SO2',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2018-12-05T11:53:01',
            _END_DATE_DKEY: '2021-02-10T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_S02_COLUMN_NUMBER_DENSITY_DKEY: 'SO2_column_number_density',
            _S05_S02_COLUMN_NUMBER_DENSITY_AMF_DKEY: 'SO2_column_number_density_amf',
            _S05_S02_SLANT_COLUMN_NUMBER_DENSITY_DKEY: 'SO2_slant_column_number_density',
            _S05_ABSORBING_AEROSOL_INDEX_DKEY: 'absorbing_aerosol_index',
            _S05_CLOUD_FRACTION_DKEY: 'cloud_fraction',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle',
            _S05_S02_COLUMN_NUMBER_DENSITY_15KM_DKEY: 'SO2_column_number_density_15km'
        }
    }, GSV_DS_SENTINEL_5_OFFL_CH4_DKEY: {  # SENTINEL 5 CH4
        _COLLECTION_ID_DKEY: 'COPERNICUS/S5P/OFFL/L3_CH4',
        _DATE_DKEY: {
            _START_DATE_DKEY: '2019-02-08T08:13:16',
            _END_DATE_DKEY: '2021-02-11T00:00:00'
        },
        _BANDS_DKEY: {
            _S05_CH4_COLUMN_VOLUME_MIXING_RATIO_DRY_AIR_DKEY: 'CH4_column_volume_mixing_ratio_dry_air',
            _S05_AEROSOL_HEIGHT_DKEY: 'aerosol_height',
            _S05_AEROSOL_OPTICAL_DEPTH_DKEY: 'aerosol_optical_depth',
            _S05_SENSOR_AZIMUTH_ANGLE_DKEY: 'sensor_azimuth_angle',
            _S05_SENSOR_ZENITH_ANGLE_DKEY: 'sensor_zenith_angle',
            _S05_SOLAR_AZIMUTH_ANGLE_DKEY: 'solar_azimuth_angle',
            _S05_SOLAR_ZENITH_ANGLE_DKEY: 'solar_zenith_angle'
        }
    },
}


# -------------------------------------------------- #
# ---------- 3. Create Internal Functions ---------- #
# -------------------------------------------------- #

# ----------------------------------------- #
# ---------- 4. Create Functions ---------- #
# ----------------------------------------- #

def prt_dict_full_data():
    print(DICT_FULL_DATASET)


def prt_dict_full_dataset(dataset_id):
    if dataset_id in DICT_FULL_DATASET.keys():
        print(DICT_FULL_DATASET[dataset_id])
    else:
        print("<" + dataset_id + "> dataset does not exist in dictionary.")


def get_default_date_range_from_dict_dataset(dataset_id):
    return [DICT_FULL_DATASET[dataset_id][_DATE_DKEY][_START_DATE_DKEY],
            DICT_FULL_DATASET[dataset_id][_DATE_DKEY][_END_DATE_DKEY]]


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
        self._dataset_id = None
        self._export_name_base = ""
        self._export_name = ""

    # ----- Print Functions (Debugging) ----- #

    def prt_image_collection(self):
        print(self._image_collection)

    def prt_date_range(self):
        print(self._collection_date_range)

    def prt_image_geometry(self):
        print(self._collection_bounds_geometry)

    def prt_image(self):
        print(self._image)

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

    def set_collection(self, dataset_id):
        """
        Set the ee.ImageCollection(), which will be used for processing
        :param dataset_id: the DICT_FULL_DATASET DKEY
        :return: Nothing
        """
        if dataset_id in DICT_FULL_DATASET.keys():  # if dataset_id in DICT_FULL_DATASET DKEY list
            self._export_name_base = DICT_FULL_DATASET[dataset_id][_COLLECTION_ID_DKEY].replace("/", "_")
            self._dataset_id = dataset_id
            # Set the _image_collection
            self._image_collection = ee.ImageCollection(DICT_FULL_DATASET[dataset_id][_COLLECTION_ID_DKEY])
            # print(self._image_collection, '\n')
            if self._collection_date_range is not None:  # Check if date range is not none
                # If True, then filter by the date range
                self._image_collection = self._image_collection.filterDate(self._collection_date_range[0],
                                                                           self._collection_date_range[1])
                self._export_name_base += "_" + self._collection_date_range[0].replace("-", "").replace(':', "") + \
                                          self._collection_date_range[1].replace("-", "").replace(':', "")
                # print(self._image_collection, '\n')
            if self._collection_bounds_geometry is not None:  # Check if geometry is not none
                # If True, then filter by geometry
                self._image_collection = self._image_collection.filterBounds(self._collection_bounds_geometry)
                # print(self._image_collection, '\n')
        else:  # if dataset_id not in FICT_FULL_DATASET DKEY list
            print("Error: Uknown Dataset.")  # print error

    def create_image_index(self, index_name, clip_image=False, G=2.5, L=1.0, C1=6, C2=7.5, px_base=PX_BASE_MEAN):
        self._export_name = self._export_name_base
        if px_base == PX_BASE_MIN:
            tmp_mean_img = self._image_collection.min()
        elif px_base == PX_BASE_MAX:
            tmp_mean_img = self._image_collection.max()
        else:
            tmp_mean_img = self._image_collection.mean()
        if index_name == BAI_INDEX:
            self._image = tmp_mean_img.expression(
                '1.0 / ((0.1 - RED)**2 + (0.06 - NIR)**2)',
                {
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_RED_DKEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY])
                }
            )
            self._export_name += '_BAI'
        elif index_name == EVI_INDEX:
            self._image = tmp_mean_img.expression(
                'G * (NIR - RED) / (NIR + C1 * RED - C2 * BLUE + L)',
                {
                    'G': G,
                    'C1': C1,
                    'C2': C2,
                    'L': L,
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_RED_DKEY]),
                    'BLUE': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_BLUE_DKEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY])
                }
            )
            self._export_name += '_EVI'
        elif index_name == EVI2_INDEX:
            self._image = tmp_mean_img.expression(
                '2.5 * (NIR - RED) / (NIR + 2.4 * RED + 1)',
                {
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_RED_DKEY]),
                    'BLUE': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_BLUE_DKEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY])
                }
            )
            self._export_name += '_EVI2'
        elif index_name == NDVI_INDEX:
            self._image = tmp_mean_img.expression(
                '(NIR - RED) / (NIR + RED)',
                {
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_RED_DKEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY])
                }
            )
            self._export_name += '_NDVI'
        elif index_name == NBR_INDEX:
            self._image = tmp_mean_img.expression(
                '(NIR - SWIR) / (NIR + SWIR)',
                {
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY]),
                    'SWIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_SWIR_1_DKEY])
                }
            )
            self._export_name += '_NBR'
        elif index_name == NBRT_INDEX:
            if _THERMAL_INFRARED_DKEY in DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY].keys():
                thermal_DKEY = _THERMAL_INFRARED_DKEY
            else:
                thermal_DKEY = _THERMAL_INFRARED_1_DKEY
            self._image = tmp_mean_img.expression(
                '(NIR - SWIR * (THERMAL/1000)) / (NIR + SWIR * (THERMAL/1000))',
                {
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_NIR_DKEY]),
                    'SWIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][_SWIR_2_DKEY]),
                    'THERMAL': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_DKEY][thermal_DKEY])
                }
            )
            self._export_name += '_NBRT'
        elif index_name == NDSI_INDEX:
            pass
        elif index_name == NDWI_INDEX:
            pass
        else:
            print("Error: Uknown Index")
            return
        if clip_image:
            if self._collection_bounds_geometry is not None:
                self._image = self._image.clip(self._collection_bounds_geometry)

    def export_to_drive(self, export_name=None, scale_m2_px=1000):
        description = self._export_name
        if export_name is not None:
            description = export_name
        task_bash = {
            'image': self._image,
            'description': description,
            'region': self._collection_bounds_geometry,
            'scale': scale_m2_px,
            'folder': 'GEE_TEST'
        }
        task = ee.batch.Export.image.toDrive(**task_bash)
        task.start()
