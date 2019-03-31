var swap = function(array, firstIndex, secondIndex) {
	var a = array[secondIndex];
	array[secondIndex] = array[firstIndex];
	array[firstIndex] = a;
};

var testArray = [7, 9, 4];
var testArray2 = [1, 2, 3];
var testArray3 = ["a", "b", "c"];
swap(testArray, 0, 1);



println(testArray);

Program.assertEqual(testArray, [9, 7, 4]);

swap(testArray2, 1, 0);
Program.assertEqual(testArray2, [2, 1, 3]);

swap(testArray3, 0, 1);
Program.assertEqual(testArray3, ["b", "a", "c"]);

