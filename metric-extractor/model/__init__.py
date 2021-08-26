from dataclasses import dataclass
from datetime import datetime
from typing import List
import faust

@dataclass
class Metadata(faust.Record):
    startPicking: str
    endPicking: str
    pickedUnitsCount: int
    unitsCount: int

@dataclass
class SG(faust.Record):
    storeId: int
    pickerId: str
    metadata: Metadata

@dataclass
class Order(faust.Record):
    sg: SG

@dataclass
class Label(faust.Record):
    key: str
    value: str

@dataclass
class Metric(faust.Record):
    name: str
    value: float
    unixTimestamp: datetime
    labels: List[Label]