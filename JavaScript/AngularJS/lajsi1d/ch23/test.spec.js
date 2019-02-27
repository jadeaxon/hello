// To run this test:
// In 1st terminal:
// webdriver-manager start
// In 2nd terminal (yes, you can open multiple terminals in WebStorm).
// protractor protractor.conf.js

describe('angularjs homepage todo list', function() {
  it('should add a todo', function() {
    // Our test interacts with the to-do list component about halfway down this page.
    browser.get('https://angularjs.org');

    // In the text field to add a new to-do, we send keystrokes to write this.
    element(by.model('todoList.todoText')).sendKeys('write first protractor test');
    // Click the add button.
    element(by.css('[value="add"]')).click();

    // Get all the elements via a repeater expression (like those used by ng-repeat).
    var todoList = element.all(by.repeater('todo in todoList.todos'));

    // Assert that there are three to-dos and that our new to-do is at the end of the list.
    expect(todoList.count()).toEqual(3);
    expect(todoList.get(2).getText()).toEqual('write first protractor test');

    // Check off our new to-do.
    todoList.get(2).element(by.css('input')).click();

    // Verify that there are now two done to-do items.
    var completedAmount = element.all(by.css('.done-true'));
    expect(completedAmount.count()).toEqual(2);
  });
});

describe('name field', function() {
  it('should receive value Jade Axon', function () {
    browser.get('https://angularjs.org');
    // Look up element by ng-model.
    element(by.model('yourName')).sendKeys('Jade Axon');
    // Find the hello message by a DOM path to it.
    var name = element(by.xpath('html/body/div[2]/div[1]/div[2]/div[2]/div/h1'));
    expect(name.getText()).toEqual('Hello Jade Axon!');
  });
});

