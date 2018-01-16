#!/usr/bin/python
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkContext
import sys

spark = SparkSession.builder.appName("Flights").getOrCreate()
sc = spark.sparkContext
sqlContext = SQLContext(sc)

df = sqlContext.read.format('csv').options(header='true', inferSchema='true').load("/home/ubuntu/proyecto/Flights.csv")

#df.printSchema()

df.createOrReplaceTempView("f")

opcion = sys.argv[1]
origen = sys.argv[2]
destino = sys.argv[3]

if opcion == "0" :
        sqlDF = spark.sql("SELECT AVG(ARR_DELAY_NEW - DEP_DELAY_NEW) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' AND (ARR_DELAY_NEW - DEP_DELAY_NEW) > 0")
elif opcion == "1":
        sqlDF = spark.sql("SELECT COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"') FROM f WHERE ((ARR_DELAY_NEW - DEP_DELAY_NEW) > 0) AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ")
elif opcion == "2":
        sqlDF = spark.sql("SELECT COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"') FROM f WHERE CANCELLED = '1' AND  ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ")
elif opcion == "3":
        sqlDF = spark.sql("SELECT CANCELLATION_CODE, COUNT (*)/ (SELECT COUNT(*) FROM f WHERE CANCELLED = '1' AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"') FROM f WHERE CANCELLED = '1' AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' GROUP BY CANCELLATION_CODE   ")
elif opcion == "4":
        sqlDF = spark.sql("SELECT AVG(DEP_DELAY_NEW) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"'")
elif opcion == "5":
        sqlDF = spark.sql("SELECT COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ) FROM f WHERE DEP_DELAY_NEW <> 0 AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ")
elif opcion == "6":
        sqlDF = spark.sql("SELECT AVG(DEP_DELAY_NEW) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' AND DEP_DELAY_NEW <>0")
elif opcion == "7":
        sqlDF = spark.sql("SELECT AVG(ARR_DELAY_NEW) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"'")
elif opcion == "8":
        sqlDF = spark.sql("SELECT COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ) FROM f WHERE ARR_DELAY_NEW <> 0 AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ")
elif opcion == "9":
        sqlDF = spark.sql("SELECT AVG(ARR_DELAY_NEW) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' AND ARR_DELAY_NEW <>0")
elif opcion == "10":
        sqlDF = spark.sql("SELECT AIRLINE_ID, AVG(ARR_DELAY_NEW - DEP_DELAY_NEW) FROM f WHERE  ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' GROUP BY AIRLINE_ID")
elif opcion == "11":
        sqlDF = spark.sql("SELECT AIRLINE_ID, AVG(ARR_DELAY_NEW - DEP_DELAY_NEW) FROM f WHERE  ((ARR_DELAY_NEW - DEP_DELAY_NEW) > 0) AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' GROUP BY AIRLINE_ID")
elif opcion == "12":
        sqlDF = spark.sql("SELECT AIRLINE_ID, COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ) FROM f WHERE ((ARR_DELAY_NEW -  DEP_DELAY_NEW > 0)) AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' GROUP BY AIRLINE_ID ")
elif opcion == "13":
        sqlDF = spark.sql("SELECT AIRLINE_ID,COUNT (*)/ (SELECT COUNT(*) FROM f WHERE ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' ) FROM f WHERE CANCELLED = '1' AND ORIGIN_CITY_MARKET_ID = '"+origen+"' AND DEST_CITY_MARKET_ID = '"+destino+"' GROUP BY AIRLINE_ID ")
else:
        print("Opcion no valida")
        opcion = -1

if opcion != -1:        
        sqlDF.show()
