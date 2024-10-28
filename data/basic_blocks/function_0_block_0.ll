None:
define spir_kernel void @sobel_filter(<4 x i8>* nocapture readonly, <4 x i8>* nocapture) local_unnamed_addr #0 !kernel_arg_addr_space !4 !kernel_arg_access_qual !5 !kernel_arg_type !6 !kernel_arg_base_type !7 !kernel_arg_type_qual !8 {
%3 = tail call i64 @_Z13get_global_idj(i32 0) #3
%4 = trunc i64 %3 to i32
%5 = tail call i64 @_Z13get_global_idj(i32 1) #3
%6 = trunc i64 %5 to i32
%7 = tail call i64 @_Z15get_global_sizej(i32 0) #3
%8 = trunc i64 %7 to i32
%9 = mul i32 %8, %6
%10 = add i32 %9, %4
%11 = icmp eq i32 %4, 0
br i1 %11, label %87, label %12
