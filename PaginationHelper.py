class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return self._item_count // self.items_per_page

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1





collection = ['a','b','c','d']
helper = PaginationHelper(collection, 4)

print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0)) # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid
print(helper.page_item_count(0)) # should == -1 since the page is invalid
# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid