import irsdk
import pandas as pd

# Path to your .ibt file
ibt_file_path = r"C:\Users\Ashton\OneDrive\Desktop\idas\fordmustanggt3_spa combined 2024-07-18 21-34-18.ibt"

ibt = irsdk.IBT()
ibt.open(ibt_file_path)

# Open the IBT file

# List of data points to extract
data_points = [
    'Speed', 'AirDensity', 'AirPressure', 'AirTemp', 'Brake', 'BrakeABSactive', 
    'BrakeRaw', 'CamCameraNumber', 'CamCameraState', 'CamCarIdx', 'CamGroupNumber', 
    'CarIdxBestLapNum', 'CarIdxBestLapTime', 'CarIdxClass', 'CarIdxClassPosition', 
    'CarIdxEstTime', 'CarIdxF2Time', 'CarIdxFastRepairsUsed', 'CarIdxGear', 'CarIdxLap', 
    'CarIdxLapCompleted', 'CarIdxLapDistPct', 'CarIdxLastLapTime', 'CarIdxOnPitRoad', 
    'CarIdxP2P_Count', 'CarIdxP2P_Status', 'CarIdxPaceFlags', 'CarIdxPaceLine', 'CarIdxPaceRow', 
    'CarIdxPosition', 'CarIdxQualTireCompound', 'CarIdxQualTireCompoundLocked', 'CarIdxRPM', 
    'CarIdxSessionFlags', 'CarIdxSteer', 'CarIdxTireCompound', 'CarIdxTrackSurface', 
    'CarIdxTrackSurfaceMaterial', 'CarLeftRight', 'ChanAvgLatency', 'ChanClockSkew', 
    'ChanLatency', 'ChanPartnerQuality', 'ChanQuality', 'Clutch', 'ClutchRaw', 'CpuUsageBG', 
    'CpuUsageFG', 'DCDriversSoFar', 'DCLapStatus', 'dcPitSpeedLimiterToggle', 'dcStarter', 
    'DisplayUnits', 'dpFastRepair', 'dpFuelAddKg', 'dpFuelAutoFillActive', 'dpFuelAutoFillEnabled', 
    'dpFuelFill', 'dpLFTireChange', 'dpLFTireColdPress', 'dpLRTireChange', 'dpLRTireColdPress', 
    'dpRFTireChange', 'dpRFTireColdPress', 'dpRRTireChange', 'dpRRTireColdPress', 'dpWindshieldTearoff', 
    'DriverMarker', 'Engine0_RPM', 'EngineWarnings', 'EnterExitReset', 'FastRepairAvailable', 
    'FastRepairUsed', 'FogLevel', 'FrameRate', 'FrontTireSetsAvailable', 'FrontTireSetsUsed', 
    'FuelLevel', 'FuelLevelPct', 'FuelPress', 'FuelUsePerHour', 'Gear', 'GpuUsage', 'HandbrakeRaw', 
    'IsDiskLoggingActive', 'IsDiskLoggingEnabled', 'IsGarageVisible', 'IsInGarage', 'IsOnTrack', 
    'IsOnTrackCar', 'IsReplayPlaying', 'Lap', 'LapBestLap', 'LapBestLapTime', 'LapBestNLapLap', 
    'LapBestNLapTime', 'LapCompleted', 'LapCurrentLapTime', 'LapDeltaToBestLap', 'LapDeltaToBestLap_DD', 
    'LapDeltaToBestLap_OK', 'LapDeltaToOptimalLap', 'LapDeltaToOptimalLap_DD', 'LapDeltaToOptimalLap_OK', 
    'LapDeltaToSessionBestLap', 'LapDeltaToSessionBestLap_DD', 'LapDeltaToSessionBestLap_OK', 
    'LapDeltaToSessionLastlLap', 'LapDeltaToSessionLastlLap_DD', 'LapDeltaToSessionLastlLap_OK', 
    'LapDeltaToSessionOptimalLap', 'LapDeltaToSessionOptimalLap_DD', 'LapDeltaToSessionOptimalLap_OK', 
    'LapDist', 'LapDistPct', 'LapLasNLapSeq', 'LapLastLapTime', 'LapLastNLapTime', 'LatAccel', 
    'LatAccel_ST', 'LeftTireSetsAvailable', 'LeftTireSetsUsed', 'LFbrakeLinePress', 'LFcoldPressure', 
    'LFshockDefl', 'LFshockDefl_ST', 'LFshockVel', 'LFshockVel_ST', 'LFtempCL', 'LFtempCM', 'LFtempCR', 
    'LFTiresAvailable', 'LFTiresUsed', 'LFwearL', 'LFwearM', 'LFwearR', 'LoadNumTextures', 'LongAccel', 
    'LongAccel_ST', 'LRbrakeLinePress', 'LRcoldPressure', 'LRshockDefl', 'LRshockDefl_ST', 'LRshockVel', 
    'LRshockVel_ST', 'LRtempCL', 'LRtempCM', 'LRtempCR', 'LRTiresAvailable', 'LRTiresUsed', 'LRwearL', 
    'LRwearM', 'LRwearR', 'ManifoldPress', 'ManualBoost', 'ManualNoBoost', 'MemPageFaultSec', 
    'MemSoftPageFaultSec', 'OilLevel', 'OilPress', 'OilTemp', 'OkToReloadTextures', 'OnPitRoad', 
    'PaceMode', 'Pitch', 'PitchRate', 'PitchRate_ST', 'PitOptRepairLeft', 'PitRepairLeft', 'PitsOpen', 
    'PitstopActive', 'PitSvFlags', 'PitSvFuel', 'PitSvLFP', 'PitSvLRP', 'PitSvRFP', 'PitSvRRP', 
    'PitSvTireCompound', 'PlayerCarClass', 'PlayerCarClassPosition', 'PlayerCarDriverIncidentCount', 
    'PlayerCarDryTireSetLimit', 'PlayerCarIdx', 'PlayerCarInPitStall', 'PlayerCarMyIncidentCount', 
    'PlayerCarPitSvStatus', 'PlayerCarPosition', 'PlayerCarPowerAdjust', 'PlayerCarSLBlinkRPM', 
    'PlayerCarSLFirstRPM', 'PlayerCarSLLastRPM', 'PlayerCarSLShiftRPM', 'PlayerCarTeamIncidentCount', 
    'PlayerCarTowTime', 'PlayerCarWeightPenalty', 'PlayerFastRepairsUsed', 'PlayerTireCompound', 
    'PlayerTrackSurface', 'PlayerTrackSurfaceMaterial', 'Precipitation', 'PushToPass', 'PushToTalk', 
    'RaceLaps', 'RadioTransmitCarIdx', 'RadioTransmitFrequencyIdx', 'RadioTransmitRadioIdx', 
    'RearTireSetsAvailable', 'RearTireSetsUsed', 'RelativeHumidity', 'ReplayFrameNum', 'ReplayFrameNumEnd', 
    'ReplayPlaySlowMotion', 'ReplayPlaySpeed', 'ReplaySessionNum', 'ReplaySessionTime', 'RFbrakeLinePress', 
    'RFcoldPressure', 'RFshockDefl', 'RFshockDefl_ST', 'RFshockVel', 'RFshockVel_ST', 'RFtempCL', 
    'RFtempCM', 'RFtempCR', 'RFTiresAvailable', 'RFTiresUsed', 'RFwearL', 'RFwearM', 'RFwearR', 
    'RightTireSetsAvailable', 'RightTireSetsUsed', 'Roll', 'RollRate', 'RollRate_ST', 'RPM', 
    'RRbrakeLinePress', 'RRcoldPressure', 'RRshockDefl', 'RRshockDefl_ST', 'RRshockVel', 'RRshockVel_ST', 
    'RRtempCL', 'RRtempCM', 'RRtempCR', 'RRTiresAvailable', 'RRTiresUsed', 'RRwearL', 'RRwearM', 'RRwearR', 
    'SessionFlags', 'SessionJokerLapsRemain', 'SessionLapsRemain', 'SessionLapsRemainEx', 'SessionLapsTotal', 
    'SessionNum', 'SessionOnJokerLap', 'SessionState', 'SessionTick', 'SessionTime', 'SessionTimeOfDay', 
    'SessionTimeRemain', 'SessionTimeTotal', 'SessionUniqueID', 'ShiftGrindRPM', 'ShiftIndicatorPct', 
    'ShiftPowerPct', 'Skies', 'SolarAltitude', 'SolarAzimuth', 'Speed', 'SteeringWheelAngle', 
    'SteeringWheelAngleMax', 'SteeringWheelLimiter', 'SteeringWheelMaxForceNm', 'SteeringWheelPctDamper', 
    'SteeringWheelPctIntensity', 'SteeringWheelPctSmoothing', 'SteeringWheelPctTorque', 
    'SteeringWheelPctTorqueSign', 'SteeringWheelPctTorqueSignStops', 'SteeringWheelPeakForceNm', 
    'SteeringWheelTorque', 'SteeringWheelTorque_ST', 'SteeringWheelUseLinear', 'Throttle', 'ThrottleRaw', 
    'TireLF_RumblePitch', 'TireLR_RumblePitch', 'TireRF_RumblePitch', 'TireRR_RumblePitch', 
    'TireSetsAvailable', 'TireSetsUsed', 'TrackTemp', 'TrackTempCrew', 'TrackWetness', 'VelocityX', 
    'VelocityX_ST', 'VelocityY', 'VelocityY_ST', 'VelocityZ', 'VelocityZ_ST', 'VertAccel', 'VertAccel_ST', 
    'VidCapActive', 'VidCapEnabled', 'Voltage', 'WaterLevel', 'WaterTemp', 'WeatherDeclaredWet', 
    'WindDir', 'WindVel', 'Yaw', 'YawNorth', 'YawRate', 'YawRate_ST'
]
# Dictionary to hold the extracted data
data = {}

# Iterate over each data point
for point in data_points:
    values = ibt.get_all(point)
    if values is not None:
        if all(isinstance(value, (int, float, bool, str, type(None))) for value in values):
            data[point] = values

# Create DataFrame from the data dictionary
df = pd.DataFrame(data)

df['SpeedMPH'] = df['Speed'] * 2.237

# Close the IBT file
ibt.close()

# Save DataFrame to a CSV file
df.to_csv('output_data_mustang.csv', index=False)