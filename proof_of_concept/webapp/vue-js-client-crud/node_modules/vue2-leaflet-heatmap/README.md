# vue2-leaflet-heatmap

This is a [heatmap](https://github.com/Leaflet/Leaflet.heat) extension for [vue2-leaflet package](https://github.com/KoRiGaN/Vue2Leaflet).

## Install

`npm i vue2-leaflet-heatmap`

## Usage

### In &lt;template&gt; add

something like this

    <l-map :zoom=10 :center="initialLocation">
      <l-tilelayer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></v-tilelayer>
      <LeafletHeatmap :lat-lng="latLngArray" :max="maxValue" :radius="15"></LeafletHeatmap>
    </l-map>

### In &lt;script&gt; add

#### option 1

In the same template file, at `<script>` part, this will make the component available only to the template in this file

    import LeafletHeatmap from './LeafletHeatmap'
    ...
    export default {
      ...
      components: {
        LeafletHeatmap
        ...
      },
      ...
    }

#### option 2

At main Vue configuration, this will make the component available to all templates in your app

    import Vue from 'vue'
    import LeafletHeatmap from './LeafletHeatmap'
    ...
    Vue.component('LeafletHeatmap', LeafletHeatmap)

### `latlngs` prop

The `lat-lng` prop needs to be an array of `LatLng` points (a polyline) with an additional third element (intensity) in each point.

### Other props

You can use the following props to style the hotline:

- **min-opacity** - the minimum opacity the heat will start at
- **max-zoom** - zoom level where the points reach maximum intensity (as intensity scales with zoom), equals `maxZoom` of the map by default
- **max** - maximum point intensity, `1.0` by default
- **radius** - radius of each "point" of the heatmap, `25` by default
- **blur** - amount of blur, `15` by default
- **gradient** - color gradient config, e.g. `{0.4: 'blue', 0.65: 'lime', 1: 'red'}`

## Author

[Jurian Baas](https://jurb.me), [Nicolò Maria Mezzopera](https://github.com/lordfuoco)

## Acknowledgements

[Nicolò Maria Mezzopera](https://github.com/lordfuoco) was nice enough to turn this into a proper npm module, thanks!

This is just a wrapper, all credit to the people who made [Leaflet](https://github.com/Leaflet) and [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat), to Korigan, who made [Vue2Leaflet](https://github.com/KoRiGaN/Vue2Leaflet), and to @jperelli and @ikmolbo for creating the [Vue2Leaflet markercluster](https://github.com/jperelli/vue2-leaflet-markercluster) and [Vue2Leaflet hotline](https://github.com/ikmolbo/vue2-leaflet-hotline) plugins.

## License

MIT
