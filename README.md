#  🌎 [A simple satellite map](https://satellite-maps.herokuapp.com/) 🌎

### To run locally:

```sh
export MAPBOX_ACCESS_TOKEN='<...>' # Get your Mapbox access token from www.mapbox.com/account
sh start.sh
```

### URL Parameters

Add lat/lon to the URL to zoom in to a given point.
- `lat`: latitude of a given point
- `lon`: longitude of a given point

Example:
```https://satellite-maps.herokuapp.com/?lon=-73.989&lat=40.733```
