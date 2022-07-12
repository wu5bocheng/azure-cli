# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from datetime import timedelta

MIN_WAIT_PERIOD = timedelta(minutes=10)
MAX_WAIT_PERIOD = timedelta(hours=24)


TELEMETRY_CACHE_DIR = 'telemetry'
TELEMETRY_NOTE_NAME = 'telemetry.txt'
TELEMETRY_LOG_NAME = 'telemetry.log'
TELEMETRY_LOG_DIR = 'logs'
