from __future__ import annotations

import typing

from . import protocol

if typing.TYPE_CHECKING:
    from pyspark import SparkContext
    from pyspark.sql.context import SQLContext
    from pyspark.sql.session import SparkSession


display: protocol.Display = None
displayHTML: protocol.DisplayHTML = None

udf: protocol.SparkFunctionUDF = None
spark: SparkSession = None
sc: SparkContext = None
sqlContext: SQLContext = None
sql: protocol.SparkSessionSQL = None
table: protocol.SparkSessionTable = None

dbutils: protocol.dbutils = None
getArgument: protocol.GetArgument = None
