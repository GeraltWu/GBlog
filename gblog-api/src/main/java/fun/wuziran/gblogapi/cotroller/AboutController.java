package fun.wuziran.gblogapi.cotroller;

import fun.wuziran.gblogapi.service.AboutService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Description
 * @Author Geralt
 * @Date 2024/7/17
 */

@RestController
public class AboutController {
    @Autowired
    AboutService aboutService;

}
