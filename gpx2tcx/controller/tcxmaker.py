from xml.dom.minidom import Document

class TCXMaker(object):

    tcx_xmldoc = Document()
    tcx_root_node = None
    course_node = None
    track_node = None

    def __init__(self):
        # 루트 노드를 만들고 설정을 한다.
        tcx_node = self.tcx_xmldoc.createElement('TrainingCenterDatabase')
        tcx_node.setAttribute('xmlns', 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2')
        tcx_node.setAttribute('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        tcx_node.setAttribute('xsi:schemaLocation', 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd')
        self.tcx_xmldoc.appendChild(tcx_node)
        self.tcx_root_node = tcx_node

        # Courses 노드를 만들어서 추가
        courses_node = self.tcx_xmldoc.createElement('Courses')
        tcx_node.appendChild(courses_node)

        # Course 노드를 만들어서 추가
        course_node = self.tcx_xmldoc.createElement('Course')
        courses_node.appendChild(course_node)
        self.course_node = course_node

        # Track 노드를 만들어서 추가
        track_node = self.tcx_xmldoc.createElement('Track')
        course_node.appendChild(track_node)
        self.track_node = track_node

    def add_name(self, name):
        course_name_node = self.tcx_xmldoc.createElement('Name')
        self.course_node.appendChild(course_name_node)

        course_name_node_text_node = self.tcx_xmldoc.createTextNode(name)
        course_name_node.appendChild(course_name_node_text_node)

        folder_node = self.tcx_xmldoc.createElement('Folders')
        self.tcx_root_node.appendChild(folder_node)

        courses_node = self.tcx_xmldoc.createElement('Courses')
        folder_node.appendChild(courses_node)

        course_folder_node = self.tcx_xmldoc.createElement('CourseFolder')
        course_folder_node.setAttribute('Name', name)
        courses_node.appendChild(course_folder_node)

        course_name_ref_node = self.tcx_xmldoc.createElement('CourseNameRef')
        course_folder_node.appendChild(course_name_ref_node)

        id_node = self.tcx_xmldoc.createElement('Id')
        course_name_ref_node.appendChild(id_node)

        id_text_node = self.tcx_xmldoc.createTextNode(name)
        id_node.appendChild(id_text_node)

    def add_lap(self, totaltime_sec, distance, begin_lat, begin_lon, end_lat, end_lon):
        # course 노드에 Lap 노드 추가
        lap_node = self.tcx_xmldoc.createElement('Lap')
        self.course_node.appendChild(lap_node)

        # TotalTimeSeconds 노드 추가
        total_time_node = self.tcx_xmldoc.createElement('TotalTimeSeconds')
        lap_node.appendChild(total_time_node)
        total_time_node_text_node = self.tcx_xmldoc.createTextNode(totaltime_sec)
        total_time_node.appendChild(total_time_node_text_node)

        # DistanceMeters 노드 추가
        distance_node = self.tcx_xmldoc.createElement('DistanceMeters')
        lap_node.appendChild(distance_node)
        distance_node_text_node = self.tcx_xmldoc.createTextNode(distance)
        distance_node.appendChild(distance_node_text_node)

        # BeginPosition 노드 추가
        begin_node = self.tcx_xmldoc.createElement('BeginPosition')
        lap_node.appendChild(begin_node)

        # LatitudeDegrees 노드 추가
        begin_lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        begin_node.appendChild(begin_lat_node)
        begin_lat_node_text_node = self.tcx_xmldoc.createTextNode(begin_lat)
        begin_lat_node.appendChild(begin_lat_node_text_node)

        # LongitudeDegrees 노드 추가
        begin_lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        begin_node.appendChild(begin_lon_node)
        begin_lon_node_text_node = self.tcx_xmldoc.createTextNode(begin_lon)
        begin_lon_node.appendChild(begin_lon_node_text_node)

        # BeginPosition 노드 추가
        end_node = self.tcx_xmldoc.createElement('EndPosition')
        lap_node.appendChild(end_node)

        # LatitudeDegrees 노드 추가
        end_lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        end_node.appendChild(end_lat_node)
        end_node_text_node = self.tcx_xmldoc.createTextNode(end_lat)
        end_lat_node.appendChild(end_node_text_node)

        # LongitudeDegrees 노드 추가
        end_lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        end_node.appendChild(end_lon_node)
        end_lon_node_text_node = self.tcx_xmldoc.createTextNode(end_lon)
        end_lon_node.appendChild(end_lon_node_text_node)

        # Intensity 노드 추가
        intensity_node = self.tcx_xmldoc.createElement('Intensity')
        lap_node.appendChild(intensity_node)
        intensity_node_text_node = self.tcx_xmldoc.createTextNode('Active')
        intensity_node.appendChild(intensity_node_text_node)

    def add_trackpoint(self, lat, lon, ele):
        # Trackpoint 노드를 만들어서 추가

        trackpoint_node = self.tcx_xmldoc.createElement('TrackPoint')
        self.track_node.appendChild(trackpoint_node)

        # Time 노드를 만들어서 추가
        time_node = self.tcx_xmldoc.createElement('Time')
        trackpoint_node.appendChild(time_node)

        # Time 값 입력
        time_text_node = self.tcx_xmldoc.createTextNode('2010-01-01T00:00:00Z')
        time_node.appendChild(time_text_node)

        # position 노드를 만들어서 추가
        position_node = self.tcx_xmldoc.createElement('Position')
        trackpoint_node.appendChild(position_node)

        # LatitudeDegrees 노드를 만들어서 추가
        lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        position_node.appendChild(lat_node)

        lat_text_node = self.tcx_xmldoc.createTextNode(lat)
        lat_node.appendChild(lat_text_node)

        # LongitudeDegrees 노드를 만들어서 추가
        lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        position_node.appendChild(lon_node)

        lon_text_node = self.tcx_xmldoc.createTextNode(lon)
        lon_node.appendChild(lon_text_node)

        # AltitudeMeters 노드를 만들어서 추가
        alt_node = self.tcx_xmldoc.createElement('AltitudeMeters')
        trackpoint_node.appendChild(alt_node)

        alt_text_node = self.tcx_xmldoc.createTextNode(ele)
        alt_node.appendChild(alt_text_node)

        # DistanceMeters 노드를 만들어서 추가
        dist_node = self.tcx_xmldoc.createElement('DistanceMeters')
        trackpoint_node.appendChild(dist_node)

    def add_coursepoint(self, lat, lon, wpt_name):
        coursepoint_node = self.tcx_xmldoc.createElement('CoursePoint')
        self.course_node.appendChild(coursepoint_node)

        wpt_name_node = self.tcx_xmldoc.createElement('Name')
        coursepoint_node.appendChild(wpt_name_node)

        wpt_name_text_node = self.tcx_xmldoc.createTextNode(wpt_name)
        wpt_name_node.appendChild(wpt_name_text_node)

        time_node = self.tcx_xmldoc.createElement('Time')
        coursepoint_node.appendChild(time_node)

        time_text_node = self.tcx_xmldoc.createTextNode('2010-01-01T01:26:32Z')
        time_node.appendChild(time_text_node)

        # position 노드를 만들어서 추가
        position_node = self.tcx_xmldoc.createElement('Position')
        coursepoint_node.appendChild(position_node)

        # LatitudeDegrees 노드를 만들어서 추가
        lat_node = self.tcx_xmldoc.createElement('LatitudeDegrees')
        position_node.appendChild(lat_node)

        lat_text_node = self.tcx_xmldoc.createTextNode(lat)
        lat_node.appendChild(lat_text_node)

        # LongitudeDegrees 노드를 만들어서 추가
        lon_node = self.tcx_xmldoc.createElement('LongitudeDegrees')
        position_node.appendChild(lon_node)

        lon_text_node = self.tcx_xmldoc.createTextNode(lon)
        lon_node.appendChild(lon_text_node)

        # position 노드를 만들어서 추가
        pointtype_node = self.tcx_xmldoc.createElement('PointType')
        coursepoint_node.appendChild(pointtype_node)

        pointtype_text_node = self.tcx_xmldoc.createTextNode('Generic')
        pointtype_node.appendChild(pointtype_text_node)

    def get_tcx(self):
        return self.tcx_xmldoc.toprettyxml(encoding='UTF-8')
