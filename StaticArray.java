/**
Array is a contiguous block of data
Static array's are fixed size.

Read O(1):
Array values are accessed using indexes
It is a constant time operation since we already have the index / memory location.

Insert at end O(1):
Static arrays are fixed size arrays. This is a limitation of static arrays.
You can only add values to an empty slot in an array. If the array is full, you cannot add
more items unless you are dynamically copying and making a new array with a hiegher length.
It is a constant time operation since we already have the index / memory location.

Delete O(1):
Delete's are not really deletes in a static array coz of the fact that you can deallocate the memory
allotted to teh full array. You can just set that particular itenm to 0, -1 or a null value.
But the array will keep occupying the same amount of memory in RAM.
It is a constant time operation since we already have the index / memory location.

Insert at arbitrary position (Beginning or middle) O(n):
Insering at an arbitrary position is not as efficient as oinserting at end.
This is because this will require us to shift / move all of the items 1 position to the right from the
insertion position. Start the shift from the left and keep shifting values which are left to the pointer
towards the right untill you reach the index where you need to add the item.

Delete at arbitrary position (Every position except end) O(n):
This will require the same procedure as the insertion at arbitrary psoition.
But since a value is being removed from an index, we would have to shift values to the left
to fill up the empty space in the array.
**/

public class StaticArray {
    // Insert the value at end
    // Insert at the next open position
    // Length is the num values in array
    // capacity is the total space allocated to the array
    // O(1)
    public void insertEnd(int[] arr, int val, int length, int capacity) {
        if(length < capacity) {
            arr[length] = val;
        }
    }

    // Remove the last value in the array
    // Don't forget to decrement length
    // O(1)
    public void removeEnd(int[] arr, int length) {
        if(length > 0) {
            arr[length] = -1;
            length--;
        }
    }

    // Insert at arbitrary position
    // This assumes position is a valid index and the array is not full
    // O(n)
    public void insertMiddle(int[] array, int position, int value, int length) {
        //shift values to right to make space
        for(int index = length - 1; index > position - 1; index--) {
            array[index + 1] = array[index];
        }

        //Insert value at position when all values have finished shifting right
        array[position] = value;
    }

    // Assuming position is valid
    // O(n)
    public void removeMiddle(int[] array, int position, int length) {
        for(int index = position + 1; index < length; index++) {
            array[index - 1] = array[index];
        }
    }

    // Print array
    // O(n)
    public void printArray(int[] array, int length) {
        for (int i = 0; i < length; i++) {
            System.out.println(array[i] + " ");
        }
        System.out.println();
    }
}
