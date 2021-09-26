#include <[LIB_H]>


void runExec(){
[HOOK]
}


void setup(){
  delay(500);
  [LIB].begin();
  pinMode(17,OUTPUT);
  pinMode(30,OUTPUT);
  delay(2500);
  runExec();
  delay(400);
  [LIB].println("[CMD]");
  //.press(KEY_RETURN);
  //KeyboardAzertyFr.releaseAll();
}
void loop(){

}
