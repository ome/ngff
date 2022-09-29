# OME-NGFF tools

Various tools are available for viewing and working with OME-NGFF data.
The following tables document which features of the OME-NGFF spec are supported by which tools.

## Viewers

| viewer | Z-downsampling                                  | omero info | multiscales factor not=2                           | URL (not s3)                                               | v0.3 axes | 3D view | labels | HCS plate |
| ------ | ----------------------------------------------- | ---------- | -------------------------------------------------- | ---------------------------------------------------------- | --------- | ------- | ------ | --------- |
| napari | y                                               | y          | y                                                  | y                                                          | y         | y (1)   | y      | y         |
| vizarr | [n](https://github.com/hms-dbmi/vizarr/pull/71) | y          | [n](https://github.com/hms-dbmi/vizarr/issues/101) | y                                                          | y         | n       | n      | y         |
| MoBIE  | y                                               | n          | y                                                  | [n](https://github.com/mobie/mobie-viewer-fiji/issues/351) | n         | y       | y      | n         |

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
      <td>n</td>
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
      <th><a href="https://github.com/ome/napari-ome-zarr/">napari-ome-zarr</a> (1)</th>
      <th><a href="https://github.com/hms-dbmi/vizarr/">vizarr</a></th>
      <th><a href="https://github.com/mobie/mobie-viewer-fiji/">MoBIE</a> (3)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>omero info</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>Z-downsampling</td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/pull/71">n</a></td>
      <td>y</td>
    </tr>
    <tr>
      <td>multiscales factor not=2</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>v0.3 axes</td>
      <td>y</td>
      <td>y</td>
      <td>?</td>
    </tr>
    <tr>
      <td>3D view</td>
      <td>y (2)</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>labels</td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>HCS plate</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>bioformats2raw.layout</td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/149">n</a></td>
      <td>n</td>
    </tr>
  </tbody>
</table>
