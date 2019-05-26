a=input('a: ');
b=input('b: ');
c=input('c: ');
ymin=input('ymin: ');
ymax=input('ymax: ');
x1=0;
x2=0;
y=0;
z1=0;
z2=0;
r1=0;
r2=0;
cp=c;

 

for q=ymin:.01:ymax
	c=cp-q;
	if q==ymin
		y(1)=q;
		r1=(-b+(b^2-4*a*c)^.5)/2/a;
		r2=(-b-(b^2-4*a*c)^.5)/2/a;
		x1(1)=real(r1);
		x2(1)=real(r2);
		z1(1)=imag(r1);
		z2(1)=imag(r2);
	else
		y(length(y)+1)=q;
		r1=(-b+(b^2-4*a*c)^.5)/2/a;
		r2=(-b-(b^2-4*a*c)^.5)/2/a;
		x1(length(x1)+1)=real(r1);
		x2(length(x2)+1)=real(r2);
		z1(length(z1)+1)=imag(r1);
		z2(length(z2)+1)=imag(r2);
	end
end
plot3(x1,z1,y,'b:','LineWidth',2);
hold on;
plot3(x2,z2,y,'b:','LineWidth',2);
hold off;
xlabel('x');
ylabel('z');
zlabel('y');
grid;
