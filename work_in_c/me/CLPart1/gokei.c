



 float heikin,goukei=0,a[10];
 int i;
for(i=0;i<10;i++) {
  printf("input a[%d]: ",i);
  scanf("%f",&a[i]);
  goukei+=a[i];
}
 heikin = goukei/10;
printf("合計 = %f,平均 = %f\n",goukei,heikin);

return 0;
}
