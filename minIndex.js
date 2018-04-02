var indexOfMinimum = function(array, startIndex) {
    // Set initial values for minValue and minIndex,
    // based on the leftmost entry in the subarray:  
    var minValue = array[startIndex];
    var minIndex = startIndex;
    var maxIndex = array.length;
    var currentVal;
    // Loop over items starting with startIndex,
    // updating minValue and minIndex as needed:
    for (var i = startIndex +1; i < maxIndex; i++){
        currentVal = array[i];
        if(currentVal < minValue){
            minIndex = i;
            minValue = array[i];
        }
    }
    return minIndex;
}; 

var array = [18, 6, 66, 44, 9, 22, 14];   
var index = indexOfMinimum(array, 2);

//  For the test array [18, 6, 66, 44, 9, 22, 14], 
//  the value 9 is the smallest of [..66, 44, 9, 22, 14]
//  Since 9 is at index 4 in the original array, 
//  "index" has value 4
println("The index of the minimum value of the subarray starting at index 2 is " + index + "."  );


Program.assertEqual(index, 4);

var array2 = [1, 2, 3, 4, 5, 6];
var index2 = indexOfMinimum(array2, 1);


println("The index of the minimum value of the subarray2 starting at index 1 is " + index2 + "."  );

Program.assertEqual(index2, 1);

var array3 = [2, 3, 4, 5, 6];
var index3 = indexOfMinimum(array3, 3);
println("The index of the minimum value of the subarray3 starting at index 1 is " + index3 + "."  );
Program.assertEqual(index3, 3);