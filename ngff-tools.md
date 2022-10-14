# OME-NGFF tools

Various tools are available for viewing and working with OME-NGFF data.
The following tables document which features of the OME-NGFF spec are supported by which tools.

## Viewers

| viewer | Z-downsampling                                  | omero info | multiscales factor not=2                           | URL (not s3)                                               | v0.3 axes | 3D view | labels | HCS plate |
| ------ | ----------------------------------------------- | ---------- | -------------------------------------------------- | ---------------------------------------------------------- | --------- | ------- | ------ | --------- |
| napari | y                                               | y          | y                                                  | y                                                          | y         | y (1)   | y      | y         |
| vizarr | [n](https://github.com/hms-dbmi/vizarr/pull/71) | y          | [n](https://github.com/hms-dbmi/vizarr/issues/101) | y                                                          | y         | n       | n      | y         |
| MoBIE  | y                                               | n          | y                                                  | [n](https://github.com/mobie/mobie-viewer-fiji/issues/351) | y         | y       | y      | n         |

1. napari 3D view only supported for lowest level of multiscales pyramid

<table>
  <thead>
    <tr>
      <th>viewer</th>
      <th>Z-downsampling</th>
      <th>omero info</th>
      <th>multiscales factor not=2</th>
      <th>URL (not s3)</th>
      <th>v0.3 axes</th>
      <th>3D view</th>
      <th>labels</th>
      <th>HCS plate</th>
      <th>bioformats2raw.layout</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/ome/napari-ome-zarr/">napari-ome-zarr</a> (1)</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y (2)</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td><a href="https://github.com/hms-dbmi/vizarr/">vizarr</a></td>
      <td><a href="https://github.com/hms-dbmi/vizarr/pull/71">n</a></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/101">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/149">n</a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/mobie/mobie-viewer-fiji/">MoBIE</a> (3)</td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td><a href="https://itkwidgets.readthedocs.io/en/latest">itkwidgets</a></td>
      <td>y</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/546">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/547">n</a></td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td><a href="https://webknossos.org">webKnossos</a></td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
    </tr>
  </tbody>
</table>

1. <a href="https://github.com/ome/napari-ome-zarr/">napari-ome-zarr</a> plugin for <a href="https://napari.org">napari</a> uses <a href="https://github.com/ome/ome-zarr-py/">ome-zarr-py</a>
2. napari 3D view only supported for lowest level of multiscales pyramid
3. MoBIE: Open with `Plugins > BigDataViewer > OME-Zarr > Open OME-Zarr From...`


<table>
  <thead>
    <tr>
      <th></th>
      <th>Sample data</th>
      <th><a href="https://github.com/ome/napari-ome-zarr/">napari-ome-zarr</a> (1)</th>
      <th><a href="https://github.com/hms-dbmi/vizarr/">vizarr</a></th>
      <th><a href="https://github.com/mobie/mobie-viewer-fiji/">MoBIE</a> (3)</th>
      <th><a href="https://itkwidgets.readthedocs.io/en/latest">itkwidgets</a></th>
      <th><a href="https://webknossos.org">webKnossos</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Z-downsampling</td>
      <td></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/pull/71">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td>omero info</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr">6001240.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/546">n</a></td>
      <td>n</td>
    </tr>
    <tr>
      <td>multiscales factor not=2</td>
      <td></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/101">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td>v0.3 axes</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.3/idr0079A/9836998.zarr">9836998.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>v0.4 axes</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td>3D view</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr">6001240.zarr</a></td>
      <td>y (2)</td>
      <td>n</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td>labels</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0052A/5514375.zarr">5514375.zarr</a></td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/547">n</a></td>
      <td>y</td>
    </tr>
    <tr>
      <td>HCS plate</td>
      <td></td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td>bioformats2raw.layout</td>
      <td></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/149">n</a></td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td>multiple 'multiscales'</td>
      <td></td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td>coordinateTransformations (datasets)</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457537.zarr">13457537.zarr</a>
        translate onto <a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y (translate)</td>
      <td>n</td>
      <td>n</td>
      <td>?</td>
      <td>?</td>
    </tr>
    <tr>
      <td>coordinateTransformations (multiscales)</td>
      <td></td>
      <td>n</td>
      <td>n</td>
      <td>?</td>
      <td>?</td>
      <td>?</td>
    </tr>
    <tr>
      <td>open multiple images (URLs)</td>
      <td></td>
      <td>y</td>
      <td>n</td>
      <td>?</td>
      <td>?</td>
      <td>y</td>
    </tr>
    <tr>
      <td>multiple Channels</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>multiple Time-points</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
    </tr>
  </tbody>
</table>
