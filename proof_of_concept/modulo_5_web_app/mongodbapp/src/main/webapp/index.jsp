<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
    <title>Leaflet.heat demo</title>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
    <script src="leaflet-heat.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<link rel = "stylesheet" href = "style.css" type = "text/css" media = "screen" />
	<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
	<script src='https://unpkg.com/vue/dist/vue.js'></script>
    <script src='https://unpkg.com/v-calendar'></script>
	<script src="javascript.js"></script>
</head>
<body onload="loadEmptyMap()">

<h1>GDP: Gathering Detection Platform</h1>

<div id="content">
	
		<div id="slider">
			<input @change="setColor()" v-model="value" type="range" id="myRange" class="mySlider" min="0" max="24" onchange="getTime()">
			<span :style="setColor()" class="rangeValue" id="range"> {{ value }} </span>
			<input type="button" id="reload" value="Reload Map" onClick="reload()">
		</div>

		<div id="map"></div>

	<div id="calendar">
		<v-calendar id="datepicker"></v-calendar>
   		<v-date-picker v-model='selectedDate' />
	</div>

</div>
<script type="module" src="main.js"></script>
</body>
</html>
