package fun.wuziran.gblog.viewbackend.annotation;

import java.lang.annotation.*;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/12/22
 */

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Admin {
    // 是否需要token验证
    boolean required() default true;
} 