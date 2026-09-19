from biupiu_geometry import Point2, orientation, polygon_area

def test_orientation():
    assert orientation(Point2(0,0), Point2(1,0), Point2(0,1)) == 1
    assert orientation(Point2(0,0), Point2(1,0), Point2(0,-1)) == -1
    assert orientation(Point2(0,0), Point2(1,0), Point2(2,0)) == 0

def test_polygon_area():
    square=[Point2(0,0),Point2(2,0),Point2(2,2),Point2(0,2)]
    assert polygon_area(square) == 4.0
