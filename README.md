#  🌎 [A simple satellite map](https://satellite-maps.herokuapp.com/) 🌎

[![Build status](https://travis-ci.com/markmisener/satellite-maps.svg?branch=master)](https://github.com/markmisener/satellite-maps/)

## Development:

### Running locally
```sh
export MAPBOX_ACCESS_TOKEN='<...>' # Get your Mapbox access token from www.mapbox.com/account
make run-local
```

### Testing

Tests will fail if coverage is under 94%.

```sh
make test
```

### URL Parameters

Add lat/lon to the URL to zoom in to a given point.
- `lat`: latitude of a given point
- `lon`: longitude of a given point

Example:
```https://satellite-maps.herokuapp.com/?lon=-73.989&lat=40.733```
