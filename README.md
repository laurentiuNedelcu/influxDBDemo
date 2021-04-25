# influxDBDemo
A simple demo of how it is working with InfluxDB and influxDBClient module. You can use this program in order to create new databases as long as you have installed influxd in your OS and the server is running. The default values for the database host is localhost and port 8086.

InfluxDBClient uses influxQL in order to communicate with this Time Series Database Management System. You will see that it is very similar to SQL, so if you are familiar with this one you should not have much problems with influxQL.

See https://docs.influxdata.com/ for more information.

The following instructions can be performed:

```
create database database_name
```
Create a new database in your InfluxDB server.

```
show databases
```
Show all databases that you have in your InfluxDB server. By default you should have one already created called '\_intern' do **not** modify it for your own good.

```
show measurements
```
Show all measurements for one specific database. Only the names of the measurements (if any) will be displayed. If you want to see the data from these measurements do a select statement.

```
select database database_name
```
From all of your databases select with which you want to work.

```
select stuff from measurement_name
```
Make a query select statement in order to get data from the database. Write directly the measurement_name, do **not** do database_name.measurement_name since you will not be able to get data for policy restrictions. This can be changed but for now in the script is disabled this option.

```
insert measurement_name key=value
```
Insert a point in the measurement of the database you are working with. If the measurement_name does not exist, InfluxDB will take care of creating it. More than one point (key=value) can be inserted separated by spaces.

```
insert default json
```
There is a default json created in utils.py to be inserted in the database for testing purposes.

```
update measurement_name key=value time
```
In order to modify a point in InfluxDB you have to insert again the same point with the new value. This means that you have to specify the measurement_name of the table, the key (which value's will be modified), the new value and the **time** when it was inserted (if not a new point will be created).

```
delete database database_name or drop database database_name
```
Delete a specified database from InfluxDB

```
delete measurement measurement_name or drop measurement measurement_name
```
Delete a specified measurement from the database you are working with

```
exit, close, quit
```
Use **one** of this commands in order to finish the program.
