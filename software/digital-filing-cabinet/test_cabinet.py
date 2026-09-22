from software.digital_filing_cabinet.cabinet import DigitalFilingCabinet,FilingRecord

def test_file_and_cross_link():
    c=DigitalFilingCabinet()
    a=c.file(FilingRecord("Paper A","PAPER","https://example.org/a","ja","CC-BY"))
    b=c.file(FilingRecord("Code Pattern","PATTERN","https://example.org/b","zh","MIT"))
    c.link(a,b,"supports")
    assert b in c.links[a]
    assert len(c.records)==2
