package com.manning.aip.ant;

import org.apache.commons.lang.StringUtils;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;

public class HelloAnt extends Activity {

   @Override
   public void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.main);

      // StringUtils is an external library dependency
      String toast = StringUtils.repeat("Hello Ant! ", 3);
      Toast.makeText(this, toast, Toast.LENGTH_LONG).show();
   }
}