import pytest


class TestShipmentInfoPage:

    @pytest.mark.regression
    def test_is_checkout_opened(self, open_shipment_info_page):
        assert open_shipment_info_page.is_submit_visible() is True

    @pytest.mark.smoke
    def test_is_cancel_visible(self, open_shipment_info_page):
        page = open_shipment_info_page
        assert page.is_submit_visible() is True

    @pytest.mark.smoke
    def test_continue_with_no_data(self, open_shipment_info_page, data_store):
        page = open_shipment_info_page
        page.click_continue()
        actual_text = page.get_error_text()
        expected_text = data_store.error_texts['first_name_error']
        assert actual_text == expected_text

    @pytest.mark.regression
    def test_add_shipping_info(self, open_shipment_info_page, data_store):
        page = open_shipment_info_page
        page.set_first_name(data_store.user_info['first_name']).set_last_name(data_store.user_info['last_name'])
        page.set_postal_code(data_store.user_info['postal_code'])
        assert page.click_continue().is_finish_visible() is True

    @pytest.mark.smoke
    def test_click_on_cart(self, open_shipment_info_page):
        assert open_shipment_info_page.is_robot_visible() is True
