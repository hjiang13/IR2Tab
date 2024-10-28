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

; <label>:12:                                     ; preds = %2
%13 = tail call i64 @_Z15get_global_sizej(i32 1) #3
%14 = trunc i64 %13 to i32
%15 = add i32 %8, -1
%16 = icmp ugt i32 %15, %4
%17 = icmp ne i32 %6, 0
%18 = and i1 %17, %16
%19 = add i32 %14, -1
%20 = icmp ugt i32 %19, %6
%21 = and i1 %18, %20
br i1 %21, label %22, label %87

; <label>:22:                                     ; preds = %12
%23 = add nsw i32 %10, -1
%24 = sub i32 %23, %8
%25 = zext i32 %24 to i64
%26 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %25
%27 = bitcast <4 x i8>* %26 to i32*
%28 = load i32, i32* %27, align 4, !tbaa !9
%29 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %28) #3
%30 = sub i32 %10, %8
%31 = zext i32 %30 to i64
%32 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %31
%33 = bitcast <4 x i8>* %32 to i32*
%34 = load i32, i32* %33, align 4, !tbaa !9
%35 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %34) #3
%36 = add nsw i32 %10, 1
%37 = sub i32 %36, %8
%38 = zext i32 %37 to i64
%39 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %38
%40 = bitcast <4 x i8>* %39 to i32*
%41 = load i32, i32* %40, align 4, !tbaa !9
%42 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %41) #3
%43 = sext i32 %23 to i64
%44 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %43
%45 = bitcast <4 x i8>* %44 to i32*
%46 = load i32, i32* %45, align 4, !tbaa !9
%47 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %46) #3
%48 = sext i32 %10 to i64
%49 = sext i32 %36 to i64
%50 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %49
%51 = bitcast <4 x i8>* %50 to i32*
%52 = load i32, i32* %51, align 4, !tbaa !9
%53 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %52) #3
%54 = add i32 %23, %8
%55 = zext i32 %54 to i64
%56 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %55
%57 = bitcast <4 x i8>* %56 to i32*
%58 = load i32, i32* %57, align 4, !tbaa !9
%59 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %58) #3
%60 = add i32 %10, %8
%61 = zext i32 %60 to i64
%62 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %61
%63 = bitcast <4 x i8>* %62 to i32*
%64 = load i32, i32* %63, align 4, !tbaa !9
%65 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %64) #3
%66 = add i32 %36, %8
%67 = zext i32 %66 to i64
%68 = getelementptr inbounds <4 x i8>, <4 x i8>* %0, i64 %67
%69 = bitcast <4 x i8>* %68 to i32*
%70 = load i32, i32* %69, align 4, !tbaa !9
%71 = tail call <4 x float> @_Z14convert_float4Dv4_h(i32 %70) #3
%72 = tail call <4 x float> @llvm.fmuladd.v4f32(<4 x float> %35, <4 x float> <float 2.000000e+00, float 2.000000e+00, float 2.000000e+00, float 2.000000e+00>, <4 x float> %29)
%73 = fadd <4 x float> %72, %42
%74 = fsub <4 x float> %73, %59
%75 = tail call <4 x float> @llvm.fmuladd.v4f32(<4 x float> %65, <4 x float> <float -2.000000e+00, float -2.000000e+00, float -2.000000e+00, float -2.000000e+00>, <4 x float> %74)
%76 = fsub <4 x float> %75, %71
%77 = fsub <4 x float> %29, %42
%78 = tail call <4 x float> @llvm.fmuladd.v4f32(<4 x float> %47, <4 x float> <float 2.000000e+00, float 2.000000e+00, float 2.000000e+00, float 2.000000e+00>, <4 x float> %77)
%79 = tail call <4 x float> @llvm.fmuladd.v4f32(<4 x float> %53, <4 x float> <float -2.000000e+00, float -2.000000e+00, float -2.000000e+00, float -2.000000e+00>, <4 x float> %78)
%80 = fadd <4 x float> %79, %59
%81 = fsub <4 x float> %80, %71
%82 = tail call <4 x float> @_Z5hypotDv4_fS_(<4 x float> %76, <4 x float> %81) #3
%83 = fdiv <4 x float> %82, <float 2.000000e+00, float 2.000000e+00, float 2.000000e+00, float 2.000000e+00>, !fpmath !12
%84 = tail call i32 @_Z14convert_uchar4Dv4_f(<4 x float> %83) #3
%85 = getelementptr inbounds <4 x i8>, <4 x i8>* %1, i64 %48
%86 = bitcast <4 x i8>* %85 to i32*
store i32 %84, i32* %86, align 4, !tbaa !9
br label %87

; <label>:87:                                     ; preds = %2, %22, %12
ret void
}
