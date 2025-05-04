package interviewPrep;

import java.util.Arrays;

public class Sorting {
    

    public int[] mergeSort(int[] array, int start, int end) {
        //base case:
        if((end - start + 1) <= 1) return array;

        int mid = (start + end) / 2;

        mergeSort(array, start, mid);
        mergeSort(array, mid + 1, end);

        merge(array, start, mid, end);

        return array;
    }

    public void merge(int[] array, int start, int mid, int end) {
        int[] left = Arrays.copyOfRange(array, start, mid + 1);
        int[] right = Arrays.copyOfRange(array, mid + 1, end + 1);

        int i = 0;
        int j = 0;
        int k = 0;

        while((i < left.length) && (j < right.length)) {
            if(left[i] < right[j]) {
                array[k] = left[i];
                i++;
            } else {
                array[k] = right[j];
                j++;
            }
            k++;
        } 

        while(i < left.length) {
            array[k] = left[i];
            i++;
            j++;
        }

        while(j < left.length) {
            array[k] = right[j];
            j++;
            k++;
        }
    }

    public int[] insertionSort(int[] array) {
        for(int i = 0; i < array.length; i++) {
            int j = i - 1;

            while(j >= 0 && array[j] > array[j + 1]) {
                int temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;

                j--;
            }
        }
        return array;
    }
}
