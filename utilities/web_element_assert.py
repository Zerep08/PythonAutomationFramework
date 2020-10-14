from assertpy import assert_that


def element_is_displayed(element):
    assert_that(element.displayed).is_equal_to(True)


def element_list_is_not_empty(element_list):
    assert_that(element_list).is_not_empty()


def element_is_equal_to_text(element, text):
    assert_that(element.text).is_equal_to(text)


def element_list_is_sorted_by_text_asc(element_list):
    text_list = []
    for element in element_list:
        text = element.get_web_element().find_element_by_class_name("inventory_item_name").text
        text_list.append(text)
    assert_that(sorted(text_list)).is_equal_to(text_list)


def element_list_is_sorted_by_text_desc(element_list):
    text_list = []
    for element in element_list:
        text = element.get_web_element().find_element_by_class_name("inventory_item_name").text
        text_list.append(text)

    assert_that(sorted(text_list, reverse=True)).is_equal_to(text_list)
