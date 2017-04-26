var arr = [9,6,2,13];
var min = [0];
var max =[0];

for
(var i=0;i<arr.length; i++){
    if
    (arr[i]<min){
    min=arr[i];
}
    if
    (arr[i]>max){
    max = arr[i];
    }
  if
    (arr[i]!== min && arr[i] !==max ){
      arr.length--;
    
    }
}
console.log (arr);
