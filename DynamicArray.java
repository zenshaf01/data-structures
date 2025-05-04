public class DynamicArray {
    int capacity;
    int length;
    int[] array;

    public DynamicArray() {
        capacity = 2;
        length = 0;
        array = new int[capacity];
    }

    /**
     * Insert at end - AKA - push
     */
    public void push(int value) {
        if(length == capacity) {
            this.resize();
        }

        array[length] = value;
        length++;
    }

    /**
     * Resize the array to double the size it was before
     * Resizing involves creating a new array and then copying
     * the elements from old to new array
     */
    public void resize() {
        capacity = capacity * 2;
        int[] newArray = new int[capacity];

        for(int i = 0; i < array.length; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
    }

    /**
     * Remove last element
     * Since we use the length property to access the last element
     * decrementing the length by 1 will make sure that element is never accessed
     */
    public void pop() {
        if(length > 0) {
            length--;
        }
    }

    public int getAtIndex(int index) {
        if(index < length) {
            return array[index];
        }

        return -1;
    }

    public void insertAtIndex(int index, int value) {
        if(index < length) {
            array[index] = value;
            return;
        }

        return; // or throw exception
    }
}
