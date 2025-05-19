import sys
from pathlib import Path
import asyncio
from loguru import logger

grandparent_folder = Path(__file__).parents[2] # 2 directories up
sys.path.append(f"{grandparent_folder}")
from src.settings import (
    QRZ_USER,
    QRZ_PASSOWRD,
    QRZ_API_KEY,
)
from src.qrz import get_qrz_session_key, get_qrz_callsign_info


async def main(debug: bool = False):
  qrz_session_key = get_qrz_session_key(username=QRZ_USER, password=QRZ_PASSOWRD, api_key=QRZ_API_KEY)
  logger.debug(f"{qrz_session_key}")


  callsign="4x5br".upper()
  # callsign="4x5dd".upper()
  info = await get_qrz_callsign_info(qrz_session_key=qrz_session_key, callsign=callsign, debug=debug)
  logger.debug(f"{info=}")


debug = True
asyncio.run(main(debug=debug))

