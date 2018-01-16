# Codigos

MANUAL DE AERODELAYS
Requisitos mínimos:
-Maquina con spark.
(ES RECOMENDABLE EJECUTAR SPARK DESDE UN CLUSTER PARA OBTENER UN RENDIMIENTO ÓPTIMO)
-S.O. Linux.
      2.  Archivos necesarios:
Es necesario contar siempre con estos 3 archivos para garantizar el correcto funcionamiento de AERODELAYS:
Menu.py
Consultas.py
Flights.csv
Los 3  archivos deben de estar siempre en el mismo directorio.
-Menu.py: muestra al usuario un menú de consultas. Lee la opción elegida por el usuario (número) con sus respectivos parámetros (origen, destino) y ejecuta a través de Spark la consulta.
-Consultas.py: ejecuta la consulta recibida por parámetro mediante un número, respecto un origen y destino también introducidos como parámetro. 
-Flights.csv: base de datos con los vuelos desde 2015 hasta 2017.
      3. Instrucciones:
Se ejecuta el programa menu.py mediante el comando “python”. 
Se visualizará un menú, solicitando una opción (disponible de la 1 a la 13). Se ha de introducir el número de la opción correspondiente. A continuación se pedirán datos adicionales para dicha consulta (origen, destino). Es importante recordar que en caso de introducir origen o destino, se ha de introducir el código numérico de la ciudad y no el nombre de la ciudad(Ver opciones en punto 5.2)
Una vez introducidos todos los campos, se pulsa enter. Los datos de la consulta saldrán de forma automática. Se representarán dentro de un cuadro, después de que Spark muestre al usuario todas las operaciones intermedias que hace hasta llegar a él.
       4. Interpretación de datos:
En los casos en los que se mide tiempo o medias de tiempo, aparecerá en pantalla un número que corresponde a los minutos.
Ejemplo: Consulta el tiempo medio de retraso en la salida en vuelos entre Seattle, WA (30559) y Washington, DC (20852). El resultado es 6,02, correspondiendo a 6,02 minutos de media por vuelo.
En caso de ser casos en los que se dan probabilidades, aparecerá en pantalla un número correspondiente al porcentaje:
Ejemplo: Consulta de la probabilidad de retraso en vuelos entre Seattle, WA (30559) y Washington, DC (20852). El resultado es 0,2234, correspondiendo a 22,34% de probabilidad de sufrir algún retraso.
La consultas que muestran datos pertenecientes a distintas aerolíneas, muestran el código de la aerolínea seguido del resultado. El código y su correspondiente nombre se puede consultar en el punto 5.3 de este documento.


     5. Correspondencias de datos:
5.1 La consulta que muestra las razones de cancelación da el porcentaje relativo a cada tipo de cancelación, los cuales pueden ser A,B,C,D según la siguiente correspondencia:



Code  Description
A   Carrier
B   Weather 
C   National Air System
D   Security
5.2 Los códigos de los aeropuertos y su correspondencia con el nombre real de  orígen y destino disponibles para realizar la consultas son:
Code    Description
30070   Kodiak, AK
30073   Deadhorse, AK
30107   Barrow, AK
30113   Bethel, AK
30135   Allentown/Bethlehem/Easton, PA
30136   Abilene, TX
30140   Albuquerque, NM
30141   Aberdeen, SD
30146   Albany, GA
30154   Nantucket, MA
30155   Waco, TX
30157   Eureka/Arcata, CA
30158   Atlantic City, NJ
30165   Adak Island, AK
30185   Alexandria, LA
30189   Colorado Springs, CO
30194   Dallas/Fort Worth, TX
30198   Pittsburgh, PA
30208   Augusta, GA
30245   King Salmon, AK
30255   Huntsville, AL
30257   Albany, NY
30268   Waterloo, IA
30279   Amarillo, TX
30285   Durango, CO
30299   Anchorage, AK
30325   Denver, CO
30333   Alpena, MI
30372   Aspen, CO
30397   Atlanta, GA (Metropolitan Area)
30408   Appleton, WI
30423   Austin, TX
30424   Wausau/Mosinee/Stevens Point, WI
30431   Asheville, NC
30434   Scranton/Wilkes-Barre, PA
30436   Tucson, AZ
30466   Phoenix, AZ
30469   Kalamazoo, MI
30476   Shreveport, LA
30529   Hartford, CT
30559   Seattle, WA
30561   Bakersfield, CA
30562   Mobile, AL
30577   Binghamton, NY
30581   Bangor, ME
30590   Bullhead City, AZ
30599   Birmingham, AL
30615   El Paso, TX
30620   Billings, MT
30627   Bismarck/Mandan, ND
30631   Bemidji, MN
30647   Cleveland, OH (Metropolitan Area)
30666   Bellingham, WA
30685   Bloomington/Normal, IL
30693   Nashville, TN
30713   Boise, ID
30721   Boston, MA (Metropolitan Area)
30728   Beaumont/Port Arthur, TX
30731   Brunswick, GA
30732   Aguadilla, PR
30739   Brainerd, MN
30747   Brownsville, TX
30779   Butte, MT
30781   Baton Rouge, LA
30785   Burlington, VT
30792   Buffalo, NY
30849   Bozeman, MT
30852   Washington, DC (Metropolitan Area)
30868   Columbia, SC
30894   Columbus, MS
30913   Cordova, AK
30918   Cedar City, UT
30928   Wichita, KS
30977   Chicago, IL
30980   Chattanooga, TN
30990   Charlottesville, VA
30994   Charleston, SC
31003   Cedar Rapids/Iowa City, IA
31013   Sault Ste. Marie, MI
31027   Clarksburg/Fairmont, WV
31049   College Station/Bryan, TX
31057   Charlotte, NC
31066   Columbus, OH
31076   Hancock/Houghton, MI
31097   Cody, WY
31122   Casper, WY
31123   St. Louis, MO
31135   Myrtle Beach, SC
31136   Jacksonville, FL
31140   Corpus Christi, TX
31146   Charleston/Dunbar, WV
31150   Columbus, GA
31205   Lake Charles, LA
31252   Daytona Beach, FL
31267   Dayton, OH
31295   Detroit, MI
31308   Dothan, AL
31336   Dillingham, AK
31337   Duluth, MN
31401   Ketchikan, AK
31423   Des Moines, IA
31447   Devils Lake, ND
31453   Houston, TX
31454   Orlando, FL
31471   Eau Claire, WI
31481   Panama City, FL
31503   Eagle, CO
31504   Valparaiso, FL
31517   Fairbanks, AK
31525   Elko, NV
31537   Elmira/Corning, NY
31577   Erie, PA
31587   Escanaba, MI
31603   Eugene, OR
31612   Evansville, IN
31617   New Bern/Morehead/Beaufort, NC
31624   Key West, FL
31637   Fargo, ND
31638   Fresno, CA
31641   Fayetteville, NC
31648   Kalispell, MT
31650   Minneapolis/St. Paul, MN
31695   Flagstaff, AZ
31703   New York City, NY (Metropolitan Area)
31714   Fort Myers, FL
31719   Fort Collins/Loveland, CO
31721   Flint, MI
31775   Sioux Falls, SD
31778   Fort Smith, AR
31823   Fort Wayne, IN
31834   Fayetteville, AR
31865   Gillette, WY
31867   Garden City, KS
31871   Greenville/Spartanburg, SC
31884   Spokane, WA
31895   Great Falls, MT
31898   Grand Forks, ND
31905   Longview, TX
31921   Grand Junction, CO
31953   Gainesville, FL
31973   Gulfport/Biloxi, MS
31977   Green Bay, WI
31980   Grand Island, NE
31982   Killeen, TX
31986   Grand Rapids, MI
31995   Greensboro/High Point, NC
31997   Gustavus, AK
32012   Gunnison, CO
32016   Guam, TT
32070   Harrisburg, PA
32129   Hibbing, MN
32134   Honolulu, HI
32156   Helena, MT
32177   Hobbs, NM
32206   Harlingen/San Benito, TX
32211   Las Vegas, NV
32250   Hyannis, MA
32255   Hays, KS
32265   Niagara Falls, NY
32280   Idaho Falls, ID
32323   Wilmington, NC
32335   Iron Mountain/Kingsfd, MI
32337   Indianapolis, IN
32343   International Falls, MN
32389   Williston, ND
32397   Ithaca/Cortland, NY
32402   Hilo, HI
32441   Jackson, WY
32448   Jackson/Vicksburg, MS
32457   San Francisco, CA (Metropolitan Area)
32467   Miami, FL (Metropolitan Area)
32474   Jefferson City/Columbia, MO
32511   Joplin, MO
32519   Jamestown, ND
32523   Juneau, AK
32547   Rochester, MN
32575   Los Angeles, CA (Metropolitan Area)
32600   Little Rock, AR
32758   Kona, HI
32884   Lansing, MI
32888   Laramie, WY
32891   Lawton/Fort Sill, OK
32896   Lubbock, TX
32898   Latrobe, PA
32945   Lexington, KY
32951   Lafayette, LA
32982   Lihue, HI
33029   Lincoln, NE
33038   Laredo, TX
33044   Louisville, KY
33076   La Crosse, WI
33105   Cincinnati, OH
33127   Lewiston, ID
33158   Midland/Odessa, TX
33184   Saginaw/Bay City/Midland, MI
33192   Sacramento, CA
33195   Tampa, FL (Metropolitan Area)
33198   Kansas City, MO
33214   San Antonio, TX
33241   Meridian, MS
         5.3 El código de la aerolínea corresponde con el nombre real según la siguiente tabla:



Code    Description
19393   Southwest Airlines Co.: WN
19690   Hawaiian Airlines Inc.: HA
19790   Delta Air Lines Inc.: DL
19805   American Airlines Inc.: AA
19930   Alaska Airlines Inc.: AS
19977   United Air Lines Inc.: UA
20304   SkyWest Airlines Inc.: OO
20366   ExpressJet Airlines Inc.: EV
20409   JetBlue Airways: B6
20416   Spirit Air Lines: NK
20436   Frontier Airlines Inc.: F9
21171   Virgin America: VX
