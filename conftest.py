from fixture.application import Application
import pytest
from fixture.application_contact import ApllicationContact

#@pytest.fixture(scope = "session")
#def app(request):
 #   fixture = Application()
  #  request.addfinalizer(fixture.destroy)
   # return fixture
#??????????????
#@pytest.fixture(scope = "session_contact")

### z filmu:
@pytest.fixture
def app(request):
  #  fixture = ApllicationContact()
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture