import unittest

from service_request import Escort, ServiceRequest, Status


class TestServiceRequest(unittest.TestCase):
    def setUp(self):
        self.escort = Escort(userId=1)
        self.request = ServiceRequest()

    def test_get_pending_request(self):
        request = self.request.getService()
        self.assertIs(request, self.request)
        self.assertEqual(request.status, "Pending")

    def test_accept_pending_request(self):
        result = self.request.acceptService(self.escort)
        self.assertEqual(result, Status("Accepted", self.escort))
        self.assertEqual(self.request.status, "Accepted")

    def test_decline_pending_request(self):
        result = self.request.denyService(self.escort)
        self.assertIsNone(result)
        self.assertEqual(self.request.status, "Declined")
