//#include <iostream>
//#include <graphics.h>
//#include <conio.h>
//using namespace std;
//int main()
//{
//	int gd = DETECT, gm;
//	intigraph(100,100,200,200);
//	delay(5000);
//	closegraph();	
//}



#include<graphics.h>
#include<conio.h>
#include<dos.h>

main()
{
   int gd = DETECT, gm, x, y, color, angle = 0;
   struct arccoordstype a, b;
   initgraph(&gd, &gm, "C:\\Turboc3\\BGI");
   delay(2000);                                                                
   while(angle<=360)
   {
      setcolor(BLACK);
      arc(getmaxx()/2,getmaxy()/2,angle,angle+2,100);
      setcolor(RED);
      getarccoords(&a);
      circle(a.xstart,a.ystart,25);
      setcolor(BLACK);
      arc(getmaxx()/2,getmaxy()/2,angle,angle+2,150);
      getarccoords(&a);
      setcolor(GREEN);
      circle(a.xstart,a.ystart,25);
      angle = angle+5;
      delay(50);
   }
   getch();
   closegraph();
}
