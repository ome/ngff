# OME-NGFF tools

Various tools are available for viewing and working with OME-NGFF data.
The following tables document which features of the OME-NGFF spec are supported by which tools.

## Viewers

The following versions of each viewer were used in testing:

 - <a href="https://napari.org">napari</a> 0.4.16 with plugin <a href="https://github.com/ome/napari-ome-zarr/">napari-ome-zarr</a>0.5.2 and <a href="https://github.com/ome/ome-zarr-py/">ome-zarr</a>0.6.0.
 - <a href="https://github.com/hms-dbmi/vizarr/">vizarr</a> using <a href="https://hms-dbmi.github.io/vizarr">current viewer</a> October 2022. Open via URL - see <a href="https://hms-dbmi.github.io/vizarr/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.3/idr0079A/9836998.zarr">example</a>.
 - <a href="https://github.com/mobie/mobie-viewer-fiji/">MoBIE</a> plugin for ImageJ/Fiji. Open with `Plugins > BigDataViewer > OME-Zarr > Open OME-Zarr From...`
 - <a href="https://itkwidgets.readthedocs.io/en/latest">itkwidgets</a>. Use in a python notebook, or open via URL: See <a href="https://kitware.github.io/itk-vtk-viewer/app/?rotate=false&fileToLoad=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr">example</a>.
 - <a href="https://webknossos.org">webKnossos</a> version 19988.
 - <a href="https://www.openmicroscopy.org/omero/">OMERO</a> with BioFormats <a href="https://github.com/ome/ZarrReader">ZarrReader</a> 0.2.0.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Sample data</th>
      <th>napari</th>
      <th>vizarr</th>
      <th>MoBIE</th>
      <th>itkwidgets</th>
      <th>webKnossos</th>
      <th>OMERO</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td>Viewer type, language</td>
      <td></td>
      <td>desktop, Python</td>
      <td>browser, JavaScript</td>
      <td>desktop, Java</td>
      <td>notebook, Python</td>
      <td>browser client + server</td>
      <td>various clients + server</td>
    </tr>
    <tr>
      <td>Z-downsampling</td>
      <td></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/pull/71">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>omero info</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr">6001240.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/546">n</a></td>
      <td>n</td>
      <td>n?</td>
    </tr>
    <tr>
      <td>multiscales factor not=2</td>
      <td></td>
      <td>y</td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/101">n</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y?</td>
    </tr>
    <tr>
      <td>axes (v0.3)</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.3/idr0079A/9836998.zarr">9836998.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>?</td>
    </tr>
    <tr>
      <td>v0.4 axes (v0.4)</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>?</td>
    </tr>
    <tr>
      <td>3D view</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr">6001240.zarr</a></td>
      <td>y (1)</td>
      <td>n</td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>labels</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0052A/5514375.zarr">5514375.zarr</a></td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
      <td><a href="https://github.com/InsightSoftwareConsortium/itkwidgets/issues/547">n</a></td>
      <td>y</td>
      <td>?</td>
    </tr>
    <tr>
      <td>HCS plate</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0001A/2551.zarr">idr0001</a></td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>bioformats2raw.layout</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.2/idr0070A/9838562.zarr">9838562.zarr</a></td>
      <td><a href="https://github.com/ome/napari-ome-zarr/issues/71">n</a></td>
      <td><a href="https://github.com/hms-dbmi/vizarr/issues/149">n</a></td>
      <td><span style="color: red">X</span></td>
      <td>n</td>
      <td>n</td>
      <td>y</td>
    </tr>
    <tr>
      <td>multiple 'multiscales'</td>
      <td></td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
      <td>n</td>
    </tr>
    <tr>
      <td>datasets coordinateTransformations (v0.4)</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457537.zarr">13457537.zarr</a>
        translate onto <a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y (scale, translate)</td>
      <td>n</td>
      <td>?</td>
      <td>y (scale)</td>
      <td>y (scale)</td>
      <td>?</td>
    </tr>
    <tr>
      <td>multiscales coordinateTransformations (v0.4)</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457539.zarr">13457539.zarr</a></td>
      <td>n</td>
      <td>n</td>
      <td>?</td>
      <td>?</td>
      <td>?</td>
      <td>?</td>
    </tr>
    <tr>
      <td>overlay multiple images</td>
      <td></td>
      <td>y</td>
      <td>n</td>
      <td>?</td>
      <td>?</td>
      <td>y</td>
      <td>n</td>
    </tr>
    <tr>
      <td>multiple Channels</td>
      <td><a href="https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457227.zarr">13457227.zarr</a></td>
      <td>y</td>
      <td>y</td>
      <td>y</td>
      <td>n</td>
      <td>y</td>
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
      <td>y</td>
    </tr>
  </tbody>
</table>



1. napari 3D view only supported for lowest level of multiscales pyramid

