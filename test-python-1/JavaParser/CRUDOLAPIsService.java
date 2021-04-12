package com.ccb.services.monetizacion.api.services;

import java.util.List;

import org.openlegacy.core.annotations.OpenlegacyDesigntime;
import org.openlegacy.core.annotations.services.Service;

import com.ccb.services.core.api.services.DefaultFormatOut;
import com.ccb.services.monetizacion.sdk.SpApisOlCrud.ResultSet;
import com.ccb.services.monetizacion.sdk.SpApisOlCrud.ResultSet1;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

/**
 *  A service interface and input/output definition for a web service.
 *  Defines the contract between the client and server. The client uses the same interface for testing the service via Java code. 
 *  The interface CRUDOLAPIsService can be customized to enabling passing parameters to the service.     
 */

@Service(name = "CRUDOLAPIs")
@OpenlegacyDesigntime(editor = "WebServiceEditor")
public interface CRUDOLAPIsService {

	public DefaultFormatOut getCRUDOLAPIs(CRUDOLAPIsIn cRUDOLAPIsIn) throws Exception;

    @Getter
    @Setter
    public static class CRUDOLAPIsIn {
        
        String format;
        
        Integer company;
        
        Integer country;
        
        String source;
        
        String ipWebservice;
        
        String requestId;
        
        String inputs;
        
        String type;
        
        String apisId;
        
        String appId;
        
        //String name;
        
        String webResource;
        
        String httpMethod;
        
        Double apiFlatRate;
        
        Double ratePerCall;
        
        //String logsName;
        
        Boolean deleted;
    }
    
    @ApiModel(value="CRUDOLAPIsOut", description="")
    @Getter
    @Setter
    public static class CRUDOLAPIsOut {
        
        @ApiModelProperty(value="Result Set")
        List<ResultSet> detail;
        
        @ApiModelProperty(value="Result Set1")
        List<ResultSet1> result;
    }
}
