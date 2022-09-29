# OME-NGFF tools

Various tools are available for viewing and working with OME-NGFF data.
The following table documents which features of the OME-NGFF spec are supported by which tools:

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
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>napari</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y (1)</td>
      <td>y</td>
      <td>y</td>
    </tr>
    <tr>
      <td>vizarr</td>
      <td>
        <a
          href="https://github.com/hms-dbmi/vizarr/pull/71"
          data-hovercard-type="pull_request"
          data-hovercard-url="/hms-dbmi/vizarr/pull/71/hovercard"
          data-turbo-frame=""
          >n</a
        >
      </td>
      <td>y</td>
      <td>
        <a
          href="https://github.com/hms-dbmi/vizarr/issues/101"
          data-hovercard-type="issue"
          data-hovercard-url="/hms-dbmi/vizarr/issues/101/hovercard"
          data-turbo-frame=""
          >n</a
        >
      </td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>MoBIE</td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
      <td>
        <a
          href="https://github.com/mobie/mobie-viewer-fiji/issues/351"
          data-hovercard-type="issue"
          data-hovercard-url="/mobie/mobie-viewer-fiji/issues/351/hovercard"
          data-turbo-frame=""
          >n</a
        >
      </td>
      <td>n</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
  </tbody>
</table>

