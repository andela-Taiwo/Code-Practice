function longest(sentence){
  var word = sentence;
  var word_array = word.split(" ");
  var len = word_array.length;
  var counter =0;
  var max= 0;
  var output = ""
  while(counter<len){
    if( (word_array[counter].toString()).length > max){
      max =(word_array[counter].toString()).length ;
      output = word_array[counter];

    }

    else{
      max=max;
      output =output;
    }

    counter = counter+1;

  }
  return output
}
