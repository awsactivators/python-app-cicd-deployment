import pytest
import requests_mock
from cicd_intro.web_scraper import parse_quotes, fetch_page

@pytest.fixture
def mock_response():
    html_content = '''
    <div>
        <span class='text'>Quote 1</span><small class='author'>Author 1</small>
        <span class='text'>Quote 2</span><small class='author'>Author 2</small>
    </div>
    '''
    return html_content

def test_parse_quotes(mock_response):
    quotes = parse_quotes(mock_response)
    assert len(quotes) == 2
    assert quotes[0] == ("Quote 1", "Author 1")
    assert quotes[1] == ("Quote 2", "Author 2")

def test_fetch_page():
    url = "http://fakeurl.com"
    with requests_mock.Mocker() as m:
        m.get(url, text='Fake Content')
        response = fetch_page(url)
        assert response == 'Fake Content'
