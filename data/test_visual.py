import pytest
from dash import Dash
from dash.testing.application_runners import import_app
from dash.testing.browser import Browser

def test_header_present():
    # Import and run the app
    app = import_app("visual")
    app.run_server(port=8051)
    
    # Create a browser instance
    browser = Browser()
    browser.visit("http://localhost:8051")
    
    # Check if header is present
    header = browser.find_by_tag("h1")
    assert len(header) == 1
    assert header.text == "Pink Morsels Sales Analysis: Impact of Price Increase"
    
    browser.quit()

def test_visualization_present():
    # Import and run the app
    app = import_app("visual")
    app.run_server(port=8052)
    
    # Create a browser instance
    browser = Browser()
    browser.visit("http://localhost:8052")
    
    # Check if visualization is present
    graph = browser.find_by_id("sales-graph")
    assert len(graph) == 1
    
    browser.quit()

if __name__ == "__main__":
    pytest.main()
